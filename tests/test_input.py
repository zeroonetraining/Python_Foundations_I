#Hashing the output as well as the correct answer prevents cheating
import hashlib
#System functions (for print capture):
import sys
from cStringIO import StringIO

#Setting up the input and output redirection:
backup_stdin = sys.stdin
backup_stdout = sys.stdout
name_input = 'Lee Cardholder'
balance_input = 120.50
sys.stdin = StringIO('{0:s}\n{1:f}'.format(name_input,balance_input))
sys.stdout = StringIO()
#The exercise script:
import exercises.input as proj_input
#Getting the printed values into a list of strings:
printed_output = sys.stdout.getvalue().lower().splitlines()
printed_output_nospaces = [''.join(line.split()) for line in printed_output]
#Closing the stream and restoring normal functionality:
sys.stdin.close()
sys.stdout.close()
sys.stdin = backup_stdin
sys.stdout = backup_stdout

#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,
                      stored_results_file=settings.stored_results_file,
                      no_upload_file=settings.upload_sentinel)

def test_name_input():
    output_name = None
    if hasattr(proj_input,'name'):
        output_name = proj_input.name
    tester.run_comparison(output_name,
                          name_input,
                          'You are not reading in user input and saving it to the `name` variable correctly.',
                          'Not yet implemented reading a name.')
def test_balance_input():
    output_balance = None
    if hasattr(proj_input,'balance'):
        output_balance = proj_input.balance
    tester.run_comparison(output_balance,
                          balance_input,
                          'You are not reading in user input and saving it to the `balance` variable correctly.',
                          'Not yet implemented reading the balance.')

