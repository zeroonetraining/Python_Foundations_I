#Hashing the output as well as the correct answer prevents cheating
import hashlib
#System functions (for print capture):
import sys
from cStringIO import StringIO

#Setting up the print capture:
backup = sys.stdout
sys.stdout = StringIO()
#The exercise script:
import exercises.strings as proj_string
#Getting the printed values into a list of strings:
printed_output = sys.stdout.getvalue().lower().splitlines()
printed_output_nospaces = [''.join(line.split()) for line in printed_output]
#Closing the stream and restoring normal functionality:
sys.stdout.close()
sys.stdout = backup

#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,
                      stored_results_file=settings.stored_results_file,
                      no_upload_file=settings.upload_sentinel)

def test_print_simple():
    printed_statements = None
    if len(printed_output_nospaces) > 0:
        printed_statements = printed_output_nospaces
    tester.run_comparison(printed_statements,
                          "changebankingforgood.",
                          'you did not print "Change Banking For Good." to the screen.',
                          'No statements have been printed.')
    
def test_print_e():
    printed_statements = None
    if len(printed_output_nospaces) > 0:
        printed_statements = printed_output_nospaces
        hashed_printed_statements = [hashlib.sha224(statement).hexdigest()
                                     for statement in printed_statements]
    tester.run_comparison(hashed_printed_statements,
                          ['20050c6679f3841e543e5f3bd23d047ebd0f7fd2c23185a97f7f9afa','90bcaa35ba7d1a0ca18cfb5ef10337737eba4b77045056b9e23efe1c'],
                          'you did not print the proper string for the digits of e to the screen.',
                          'No statements have been printed.')

def test_lower():
    lowered_string = None
    if hasattr(proj_string,'lower_case_string') and proj_string.lower_case_string is not None:
        lowered_string = hashlib.sha224(
            proj_string.lower_case_string).hexdigest()
    tester.run_comparison(lowered_string,
                          'c520b14db17ae59ee157c05720a62dcb7f61c3bc9f14f78ed9404336',
                          'lower_case_string does not contain a lower-cased version of '\
                          'mixed_case_string.',
                          'No value has been entered for lower_case_string.')

def test_num_branches():
    num_branches = None
    if hasattr(proj_string,'num_branches') and proj_string.num_branches is not None:
        num_branches = hashlib.sha224(
            proj_string.num_branches).hexdigest()
    tester.run_comparison(num_branches,
                          '542dc0f1b2d1f4a1d6f2d5f16aaffcffebb5362b3de4b9e74f827adb',
                          'num_branches does not contain the correct part of wiki_intro '\
                          '- did you remember that strings are zero-indexed?',
                          'No value has been entered for num_branches.')

def test_wiki_nospaces():
    wiki_intro_nospaces = None
    if hasattr(proj_string,'wiki_intro_nospaces') and proj_string.wiki_intro_nospaces is not None:
        wiki_intro_nospaces = hashlib.sha224(
            proj_string.wiki_intro_nospaces).hexdigest()
    tester.run_comparison(wiki_intro_nospaces,
                          'df597101864d6a5fed566335bcd7b992049cb0a31c8d80fec1522bf5',
                          'wiki_intro_nospaces does not contain a copy of wiki_intro with no'\
                          ' spaces - remember, there must be *ZERO* spaces.',
                          'No value has been entered for wiki_intro_nospaces.')
    
        
    

