#A library of helper functions for actually running the tests.
import numpy as np
import os
import shlex
import subprocess
import re
import datetime as dt
import sys
import logging
import json
import warnings
import inspect

import requests

import settings

#Ensure that warnings are always triggered, except for FutureWarnings which are ignored
warnings.simplefilter('always')
warnings.simplefilter(action = 'ignore', category = FutureWarning)
#Disable logging from requests for anything below something super bad, so students won't be able to see that we're sending info :)
logging.getLogger("requests").setLevel(logging.CRITICAL)

class TestClass(object):
    '''
    A class that holds information about the user and the project, so the helper functions that do the actual assertions don't need to take in a million parameters.
    '''

    def __init__(self, project_item, project_name, stored_results_file='.stored_test_results.nogit', no_upload_file='.dnu.nogit'):
        '''
        Initialize class variables necessary for uploading test results, then test to see if there is a connection to the server. If connection, check and see if there's a backlog of test results and upload those.

        Arguments:
        project_item: The course ID of the project (in COU).
        project_name: The text name of the project (e.g. Moving Data).
        stored_results_file (.stored_test_results.nogit): Where to put test results if you can't upload them to the server at this time.
        no_upload_file (.dnu.nogit): If this file exists, turn off the uploads.

        '''
        self.project_item = project_item
        self.project_name = project_name
        #Set the EID of the user based on their username on their computer, or AAAAAA if there isn't a user environment variable:
        self.eid = 'aaaaaa'
        try:
            if 'USER' in os.environ.keys():#Mac or Unix
                self.eid = os.environ['USER'].lower()
            else:#PC (at least using git bash)
                self.eid = os.environ['USERNAME'].lower()
        except KeyError:
            pass
        #Set the timestamp to attach to all the tests, in ISO 8601 format:
        dt.microsecond=0
        self.currtime = dt.datetime.utcnow().isoformat('T').split('.')[0]#The split('.')[0] just floors away the milliseconds
        self.stored_results_file = stored_results_file
        self.no_upload_file = no_upload_file

        #ElasticSearch server parameters:
        self.elasticsearch_rooturl = settings.ES_rooturl
        self.elasticsearch_index = settings.ES_index
        self.elasticsearch_type = settings.ES_type

        #Get the name of the file running the tests:
        self.calling_test = ''
        try:
            self.calling_test = os.path.basename(inspect.stack()[1][1])
        except:
            pass#If there's any error, just don't do it.
            
        #Try to connect to the server:
        self.can_connect = True
        try:
            trial_connection = requests.get(self.elasticsearch_rooturl,timeout=3)
        except:#Let's make this *any* exception, which I think makes sense here (requests.ConnectionError,requests.LocationParseError):
            self.can_connect = False

        #Turn off uploads if no_upload_file exists:
        if os.path.isfile(self.no_upload_file) == True:
            self.can_connect = False
            
        #Check if stored results file exists, and if it does and there is a connection go through the lines in the file and upload the data.
        if self.can_connect == True:#Superfluous since direct_result checks for this too, but could save some time.
            if os.path.isfile(self.stored_results_file):#Ignoring race conditions and the possibility that the program won't have read/write access to the file...
                #Load data from the file into memory
                with open(self.stored_results_file,'rb') as f:
                        result_list = f.read().splitlines()
                #Delete file contents
                with open(self.stored_results_file,'wb') as f:
                        pass
                #For each line in file, run the direct_result function.
                for line in result_list:
                        #print line
                        self.direct_payload(line)


    def create_upload_payload(self,test_result,n_steps_removed=3):
        '''
        Create a payload for uploading a test result.

        Arguments:
        test_result: The result of the test, as a descriptive string.
        n_steps_removed: How deep into the call stack to go to fetch the name of the test function.

        Returns:
        result_payload: A stringified dictionary of the test results.
        '''
        calling_function_name = sys._getframe(n_steps_removed).f_code.co_name#Gets the name of the function
        result_dict = {
            "course_slug": self.project_item,
            "project_name": self.project_name,
            "timestamp": self.currtime,
            "value": test_result,
            "eid": self.eid,
            "test_name": calling_function_name,
            "test_script":self.calling_test
        }

        return json.dumps(result_dict)

    def direct_payload(self,result_payload):
        '''
        Either upload the payload to the server, or store it in a file for later.

        Arguments:
        result_payload: A stringified dictionary, most likely the output of self.create_upload_payload.

        Returns:
        None
        '''
        successful_post = False
        if self.can_connect == True:#If you can connect, upload the data
            url = "{0:s}/{1:s}/{2:s}".format(self.elasticsearch_rooturl,self.elasticsearch_index,self.elasticsearch_type)
            try:
                r = requests.post(url,data=result_payload)
                #print result_payload
                #Check and see if the post was successful:
                if r.status_code == 201:#201 because ES returns a URI for the uploaded data
                    successful_post = True
            except:#Again, here let's be very conservative here. requests.ConnectionError:
                self.can_connect = False
            
        if self.can_connect == False or successful_post == False: #If you can't connect or the request fails, save the results to the stored results file
            with open(self.stored_results_file,'ab') as f:
                f.write(result_payload+"\n")

    def create_direct_payload(self,test_result,call_stack_levels=3):
        '''
        A simple wrapper for running create_payload and then direct_payload.

        Arguments:
        test_result: The result of the test, as a descriptive string.
        call_stack_levels: How far in the call stack you'll need to go to get the test function name.

        Returns:
        None
        '''
        result_payload = self.create_upload_payload(test_result,n_steps_removed=call_stack_levels) #Get string for uploading
        self.direct_payload(result_payload)
        
    def run_comparison(self, output,answers, incorrect_string,
                       warning_string, num_levels=3,
                       suppress_uploads=False):
        '''
        Compare answers to the output, and report the results properly.

        Arguments:
        output: The output of the function. If it's an iterable, if one
            of the values matches any of the answers, pass the test.
        answers: The correct answer, or an iterable of possible correct answers.
        incorrect_string: What to print if the output is incorrect.
        warning_string: What to print if the output is None.
        num_levels (3): How many levels deep in the call stack you'll need to go to find the test function that called this helper function (for proper test identification in the dashboard).
        suppress_uploads (False): If True, don't even try to upload the results.
            (Good for helper functions that make sure code's not super broken.)

        Example:
        run_comparison(7,[1,2,3,5,7,9,11],'You did not enter one of the first seven primes!', 'type_prime is not implemented')
        1. Tests if [1,2,3,5,7,9,11] is iterable. If it's not, it encloses it in a list.
        2. Iterates through the iterable and tests to see if at least one of the answers matches the output from the user.
        3. Runs the assertion based on the results of #2, finds True. 
        '''
        #Set default test result value:
        test_result = 'Incomplete'
        if output is not None:
            one_passed = False
            test_result = 'Fail'
            if hasattr(output,'__iter__') == False:
                output = [output]
            if hasattr(answers,'__iter__') == False:
                answers = [answers]
            for answer in answers:
                for output_single in output:
                    if output_single == answer:
                        one_passed = True
                        test_result = 'Pass'
                        break
            if suppress_uploads != True:
                self.create_direct_payload(test_result,call_stack_levels=num_levels)
            assert one_passed,incorrect_string
        else:
            warnings.warn(warning_string,UserWarning)
            if suppress_uploads != True:
                self.create_direct_payload(test_result,call_stack_levels=num_levels)
    
    def run_container_comparison(self,output,answer,incorrect_string,warning_string):
        '''
        Compare the answer to the output when they are iterable containers, and report the results properly. Note that this is only somewhat data type sensitive - a dict with the same values as a list will return False, while a numpy array with the same values/order as a list will return True (Note that edge cases for this function haven't been fully tested yet, so be a little careful with it). 

        Arguments:
        output: The output of the function.
        answer: The correct answer.
        incorrect_string: What to print if the output is incorrect.
        warning_string: What to print if the output is None.

        Example:
        run_container_comparison([1,2,3],[4,5,6],'incorrect','not implemented') raises an assertion error
        run_container_comparison([1,2,3],[1,2,5],'incorrect','not implemented') raises an assertion error
        run_container_comparison([1,2,3],[2,3,1],'incorrect','not implemented') raises an assertion error
        run_container_comparison(None,[1,2,3],'incorrect','not implemented') raises a warning
        run_container_comparison([1,2,3],[1,2,3],'incorrect','not implemented') passes
        '''
        #Set default test result value:
        test_result = 'Incomplete'
        
        if output is not None:
            test_result = 'Fail'
            try:
                if np.array_equal(output,answer) == True:
                    test_result = 'Pass'
                
                self.create_direct_payload(test_result)
                assert np.array_equal(output,answer),incorrect_string
            except AssertionError:
                #print "Expected:"
                #print answer
                #print "Received:"
                #print output
                raise
        else:
            warnings.warn(warning_string,UserWarning)
            self.create_direct_payload(test_result)

        
    def run_comparison_regex(self,output, regex_string, incorrect_string, warning_string, strip_whitespace=True, force_lowercase=True):
        '''
        Compare the output to a regular expression, and report the result properly.

        Arguments:
        output: The output of the user's function.
        regex_string: The string regular expression to use.
        incorrect_string: What to print if the output is incorrect.
        warning_string: What to print if the function hasn't been implemented yet (output is None).
        strip_whitespace(True): Should all the whitespace be stripped from the output before the regex is run?
        force_lowercase(True): Should the output be forced to lower case before the regex is run?

        Example:
        run_comparison_regex('select mrch_pstl_cd from t2_postd_trxn where trxn_amt = 10;',r'where[\a-z]+=10','incorrect','not implemented') will pass the test because the first argument (the output string) contains a where clause where some column = 10.
        '''
        if output is not None:
            #strip whitespace, if necessary:
            if strip_whitespace:
                output = output.replace(' ','')
            #Cast to lowercase, if necessary:
            if force_lowercase:
                output = output.lower()
            #Run a regex match to see if the command is present:
            regex = re.compile(regex_string)
            m = regex.search(output)
            #If the regex is present, pass true. Otherwise, pass false.
            if m is not None:
                output = True
            else:
                output = False
        self.run_comparison(output,True,incorrect_string,warning_string,num_levels=4)

    
def try_system_cmd(test_cmd,filename_to_replace,test_array,throw_error_if_no_filename=True,**kwargs):
    '''
    try to run a student's unix command on a test file.

    Arguments:
    test_cmd: The unix command that the student has entered.
    filename_to_replace: The base filename to replace with the test file.
    test_array: A numpy array of data to be written to the test file.
    throw_error_if_no_filename (True): Should you throw an error if no file is found, or just append the new_filepath on the end of the string?
    **kwargs: Valid np.savetxt keyword arguments

    Returns:
    cmd_output: The result of the command, or None if there is an error.

    Example:
    try_system_cmd('wc -l < /user/users/file.txt','file.txt',np.arange(20),delimiter=','):
    1. runs np.savetxt('test_file_temporary.nogit',np.arange(20),delimiter=',')
    2. runs wc -l < test_file_temporary.nogit, saves output as cmd_output.
    3. returns cmd_output.
    '''
    cmd_output = None
    try:
        testfile = 'test_file_temporary.nogit'
        test_cmd = replace_filename(test_cmd,filename_to_replace,testfile,throw_error_if_no_filename=throw_error_if_no_filename)
        np.savetxt(testfile,test_array,**kwargs)
        cmd_popen = subprocess.Popen(shlex.split(test_cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_output = cmd_popen.communicate()[0] 
    except:
        raise
    finally:
        os.remove(testfile)
    return cmd_output

def replace_filename(input_string,original_filename,new_filepath,throw_error_if_no_filename=True):
    '''
    Parse a string looking for a filepath using a regex, then replace that filepath with a new filepath.

    Arguments:
    input_string: The string to parse, (hopefully) containing a filepath.
    original_filename: The filename we're looking to replace, with no path - i.e. if the file is in /user/users/temp.txt, just temp.txt.
    new_filepath: The filepath to use as a replacement in the string.
    throw_error_if_no_filename(True): Should you throw an error if no file is found, or just append the new_filepath on the end of the string?

    Returns:
    replaced_string: The input string with the filename switched.

    Examples:
    replace_filename('grep ^12902 /user/users/temp/hello.txt','hello.txt','./test.txt') = 'grep ^12902 ./test.txt'
    replace_filename('grep ^12902 hello.txt','hello.txt','woo/test.txt') = 'grep ^12902 woo/test.txt'
    '''

    regex = re.compile(r"""
    (?P<prefix>^[\S\s]*)               #Catching any characters before the filename
    (?P<leading_space>^|\s)            #Forces the filename to be at the start of the string or have a leading space
    (?P<filepath>\S*{0:s})      #Matches the path, assuming no spaces
    (?P<suffix>[\S\s]*$)               #Catching any characters after the filename (trailing space not enforced)
    """.format(original_filename), re.VERBOSE)
    search_results = regex.search(input_string)
    if search_results is None:
        if throw_error_if_no_filename:
            raise ValueError('replace_filename: Could not find filename {0:s} in string {1:s}. Could you be using spaces in your file paths?'.format(original_filename,input_string))
        return input_string + " " + new_filepath
    else:
        return search_results.group('prefix') + search_results.group('leading_space') + new_filepath + search_results.group('suffix')

    
