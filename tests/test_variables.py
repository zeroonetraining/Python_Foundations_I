#Hashing the output as well as the correct answer prevents cheating
import hashlib

#The exercise script:
import exercises.variables as var
#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,stored_results_file=settings.stored_results_file,no_upload_file=settings.upload_sentinel)

def test_name():
    name = None
    if hasattr(var,'name'):
        name = var.name
    tester.run_comparison(name,
                          'Lee Cardholder',
                          "The value of the 'name' variable is incorrect.",
                          "The 'name' variable has not been set yet.")

def test_balance():
    balance = None
    if hasattr(var,'balance'):
        balance = var.balance
    tester.run_comparison(balance,
                          120.5,
                          "The value of the 'balance' variable is incorrect.",
                          "The 'balance' variable has not been set yet.")

def test_percent_apr():
    percent_apr = None
    if hasattr(var,'percent_apr'):
        percent_apr = var.percent_apr
    tester.run_comparison(percent_apr,
                          20,
                          "The value of the 'percent_apr' variable is incorrect.",
                          "The 'percent_apr' variable has not been set yet.")

def test_monthly_interest():
    monthly_interest = None
    if hasattr(var,'monthly_interest') and var.monthly_interest is not None:
        monthly_interest = hashlib.sha224('{0:f}'.format(round(var.monthly_interest,2))).hexdigest()
    tester.run_comparison(monthly_interest,
                          '184d2d7131e96e0cbb9aa38657cce73ad01c9a3cdb359e00a0c70570',
                          "The value of the 'monthly_interest' variable is incorrect.",
                          "The 'monthly_interest' variable has not been set yet.")


    

