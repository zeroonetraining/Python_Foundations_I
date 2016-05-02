#Hashing the output as well as the correct answer prevents cheating
import hashlib
#System functions (for editing the project file):
import sys
import inspect
import re

#The exercise script:
import exercises.comparisons as comparisons

#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,
                      stored_results_file=settings.stored_results_file,
                      no_upload_file=settings.upload_sentinel)

code_line_list = inspect.getsource(comparisons).splitlines()
    
def safe_code_split(code_line_list, split_regex_string, failure_return=None):
    '''
    Runs through a list of lines of code until it finds
    one that contains a match to a regex, then splits on it.
    It then checks to make sure that both sides of the code
    work on their own, and if not it will return a specified
    failure state.

    Arguments:
    code_line_list: a list of lines of code, one line per row.
    split_regex_string: The string to be used to create the regex
        to determine where to split the code.
    failure_return (None): What to return if any part of this process,
        including testing to make sure that the code works both before
        and after the split, fails.

    Returns:
    Either failure_return (if something goes wrong), or a tuple of
       (code list before split, code list after split [including
       the line that gets split on])
    
    '''

    #Find the first match, or return None
    regex = re.compile(split_regex_string)
    for i,line in enumerate(code_line_list):
        if regex.search(line) is not None:
            #Split the list:
            prefix_line_list = code_line_list[:i]
            postfix_line_list = code_line_list[i:]
            #Test the pre and post code to make sure
            #it can run separately:
            prefix_code = "\n".join(prefix_line_list)
            postfix_code = "\n".join(postfix_line_list)
            try:
                exec prefix_code
                exec postfix_code
            except:
                return failure_return
            return prefix_line_list,postfix_line_list
    return failure_return

def split_helper(code_line_list, split_regex_string,failure_return = None):
    '''
    A wrapper around the safe_code_split_function that actually
    runs the test.

    Arguments:
    SAME AS safe_code_split():

    Returns:
    post_split_lines: The lines that are after the split.
    '''
    split_code = safe_code_split(code_line_list, split_regex_string,
                                 failure_return=failure_return)
    tester.run_comparison(split_code != failure_return,
                          True,
                          "There is something preventing the tests from running properly. If you have substantively modified the structure of the exercise script, please revert the script back to its original structure.",
                          "",
                          suppress_uploads=True)
    exec "\n".join(split_code[0])
    return split_code[1]
    
def credit_description_helper(FICO, correct_result, lines_to_exec, credit_description):
    '''
    A helper function for the credit description tests:
    FICO: the FICO score to check.
    correct_result: what the output should be.
    lines_to_exec: a list of lines of code to execute
    credit_description: the default value of the target variable

    Returns:
    None
    '''
    #print "DEBUG",credit_description
    exec "\n".join(lines_to_exec)
    #print FICO,credit_description
    try:
        credit_description = credit_description.lower()
    except:
        pass
    #print "DEBUG",credit_description, correct_result
    tester.run_comparison(credit_description,
                          correct_result,
                          "credit_description gives '{0}' when FICO is {1}".format(credit_description, FICO),
                          "Haven't yet implemented credit_decision logic.",
                          num_levels=4)
    

def test_mortgage_approved_logic_not_long_standing_not_superprime():
    split_regex_string = 'mortgage_approved[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    superprime = False
    long_standing_customer = False
    large_down_payment = True
    mortgage_approved = None
    exec "\n".join(post_split_lines)
    tester.run_comparison(mortgage_approved,
                          False,
                          "mortgage_approved gives incorrect value when superprime = False, long_standing_customer = False, and large_down_payment = True",
                          "Haven't yet implemented mortgage_approved.")
    
def test_mortgage_approved_logic_not_large_down_not_superprime():
    split_regex_string = 'mortgage_approved[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    superprime = False
    long_standing_customer = True
    large_down_payment = False
    mortgage_approved = None
    exec "\n".join(post_split_lines)
    tester.run_comparison(mortgage_approved,
                          False,
                          "mortgage_approved gives incorrect value when superprime = False, long_standing_customer = True, and large_down_payment = False",
                          "Haven't yet implemented mortgage_approved.")
    
def test_mortgage_approved_logic_not_long_standing_not_large_down():
    split_regex_string = 'mortgage_approved[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    superprime = True
    long_standing_customer = False
    large_down_payment = False
    mortgage_approved = None
    exec "\n".join(post_split_lines)
    tester.run_comparison(mortgage_approved,
                          True,
                          "mortgage_approved gives incorrect value when superprime = True, long_standing_customer = False, and large_down_payment = False",
                          "Haven't yet implemented mortgage_approved.")
    
def test_mortgage_approved_logic_not_superprime():
    split_regex_string = 'mortgage_approved[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    superprime = False
    long_standing_customer = True
    large_down_payment = True
    mortgage_approved = None
    exec "\n".join(post_split_lines)
    tester.run_comparison(mortgage_approved,
                          True,
                          "mortgage_approved gives incorrect value when superprime = False, long_standing_customer = True, and large_down_payment = True",
                          "Haven't yet implemented mortgage_approved.")

    
def test_credit_description_7000():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(7000,'good',post_split_lines[1:],
                                  credit_description)
def test_credit_description_800():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(800,'good',post_split_lines[1:],
                                  credit_description)
def test_credit_description_750():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(750,'good',post_split_lines[1:],
                                  credit_description)
def test_credit_description_700():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(700,'good',post_split_lines[1:],
                                  credit_description)

def test_credit_description_699():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(699,'ok',post_split_lines[1:],
                                  credit_description)
def test_credit_description_650():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(650,'ok',post_split_lines[1:],
                                  credit_description)
def test_credit_description_600():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(600,'ok',post_split_lines[1:],
                                  credit_description)
        
def test_credit_description_599():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(599,'bad',post_split_lines[1:],
                                  credit_description)        
def test_credit_description_500():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(500,'bad',post_split_lines[1:],
                                  credit_description)   
def test_credit_description_450():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(450,'bad',post_split_lines[1:],
                                  credit_description)   
def test_credit_description_0():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(0,'bad',post_split_lines[1:],
                                  credit_description)   
def test_credit_description_neg500():
    split_regex_string = 'FICO[ ]*?=[ ]*?'
    post_split_lines = split_helper(code_line_list, split_regex_string,
                                    failure_return = None)
    credit_description = None #Default value if not implemented
    if len(post_split_lines) > 0:
        credit_description_helper(-500,'bad',post_split_lines[1:],
                                  credit_description)
    
