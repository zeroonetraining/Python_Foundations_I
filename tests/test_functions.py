#Hashing the output as well as the correct answer prevents cheating
import hashlib

#The exercise script:
import exercises.functions as proj_functions
#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,stored_results_file=settings.stored_results_file,no_upload_file=settings.upload_sentinel)

def test_compute_monthly_interest_500_1999():
    output = proj_functions.compute_monthly_interest(500,19.99)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 8.33
    tester.run_comparison(output,
                          correct_output,
                          "'compute_monthly_interest' gives an incorrect"\
                          ' result when balance = 500.00 and apr_percent = 19.99',
                          "'compute_monthly_interest' has not yet been"\
                          ' implemented')
def test_compute_monthly_interest_500_19():
    output = proj_functions.compute_monthly_interest(500,19)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 7.92
    tester.run_comparison(output,
                          correct_output,
                          "'compute_monthly_interest' gives an incorrect"\
                          ' result when balance = 500.00 and apr_percent = 19',
                          "'compute_monthly_interest' has not yet been"\
                          ' implemented')
def test_compute_monthly_interest_500_0():
    output = proj_functions.compute_monthly_interest(500,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 0.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_monthly_interest' gives an incorrect"\
                          ' result when balance = 500.00 and apr_percent = 0',
                          "'compute_monthly_interest' has not yet been"\
                          ' implemented')
def test_compute_monthly_interest_0_1999():
    output = proj_functions.compute_monthly_interest(0,19.99)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 0.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_monthly_interest' gives an incorrect"\
                          ' result when balance = 0.00 and apr_percent = 19.99',
                          "'compute_monthly_interest' has not yet been"\
                          ' implemented')
def test_compute_monthly_interest_0_0():
    output = proj_functions.compute_monthly_interest(0,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 0.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_monthly_interest' gives an incorrect"\
                          ' result when balance = 0.00 and apr_percent = 0.00',
                          "'compute_monthly_interest' has not yet been"\
                          ' implemented')


def test_compute_min_pay_500_0():
    output = proj_functions.compute_min_pay(500,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 25.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 500.00 and interest = 0.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_5_0():
    output = proj_functions.compute_min_pay(5,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 5.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 5.00 and interest = 0.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_5_2():
    output = proj_functions.compute_min_pay(5,2)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 7.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 5.00 and interest = 2.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_500_30():
    output = proj_functions.compute_min_pay(500,30)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 35.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 500.00 and interest = 30.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_5000_0():
    output = proj_functions.compute_min_pay(5000,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 50.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 5000.00 and interest = 0.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_5000_17():
    output = proj_functions.compute_min_pay(5000,17)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 67.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 5000.00 and interest = 17.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_0_0():
    output = proj_functions.compute_min_pay(0,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 0.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 0.00 and interest = 0.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_0_325():
    output = proj_functions.compute_min_pay(0,32.5)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 32.50
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = 0.00 and interest = 32.50',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')
def test_compute_min_pay_neg500_0():
    output = proj_functions.compute_min_pay(-500,0)
    try:
        output = round(output,2)
    except:
        pass
    correct_output = 0.00
    tester.run_comparison(output,
                          correct_output,
                          "'compute_min_pay' gives an incorrect"\
                          ' result when balance = -500.00 and interest = 0.00',
                          "'compute_min_pay' has not yet been"\
                          ' implemented')


                          
def test_compute_min_pay_list_normal_list():
    balance_list = [0,20,50,100,200,1000,4000]
    output = proj_functions.compute_min_pay_list(balance_list)
    try:
        output = [round(amount,2) for amount in output]
    except:
        pass
    correct_output = [0.00,20.33,25.00,25.00,25.00,26.66,106.63]
    tester.run_container_comparison(output,
                          correct_output,
                          "'compute_min_pay_list' gives an incorrect"\
                          ' result when balance_list = [0.00,20.00,50.00,100.00,200.00,300.00,400.00] and default interest',
                          "'compute_min_pay_list' has not yet been"\
                          ' implemented')
def test_compute_min_pay_list_normal_list_different_interest():
    balance_list = [0,20,50,100,200,1000,4000]
    output = proj_functions.compute_min_pay_list(balance_list,apr_percent=15)
    try:
        output = [round(amount,2) for amount in output]
    except:
        pass
    correct_output = [0.00,20.25,25.00,25.00,25.00,25.00,90.00]
    tester.run_container_comparison(output,
                          correct_output,
                          "'compute_min_pay_list' gives an incorrect"\
                          ' result when balance_list = [0.00,20.00,50.00,100.00,200.00,300.00,400.00] and apr_percent=15',
                          "'compute_min_pay_list' has not yet been"\
                          ' implemented')


def test_create_lambda_is_lambda():
    output = None
    if hasattr(proj_functions,'create_lambda') and proj_functions.create_lambda() is not None:
        try:
            output = proj_functions.create_lambda().__name__
        except:
            output = False
    tester.run_comparison(output,
                          '<lambda>',
                          "'create_lambda' does not return a lambda",
                          "'create_lambda' has not yet been implemented")
def test_create_lambda_rand_inputs_1():
    output = None
    slope = 2
    intercept = 3
    xval = 5
    if hasattr(proj_functions,'create_lambda') and proj_functions.create_lambda() is not None:
        try:
            output = hashlib.sha224(str(round(
                proj_functions.create_lambda()(slope, intercept, xval),2))).hexdigest()
        except:
            output = False
    tester.run_comparison(output,
                          'bf5271e63a05f3a0312a6401463ede47e07208b9df0571951e655c14',
                          "The lambda function made by 'create_lambda' gives incorrect answer for slope={0},"\
                          " intercept={1}, and x-value={2}".format(slope,intercept,xval),
                          "'create_lambda' has not yet been implemented")
def test_create_lambda_rand_inputs_2():
    output = None
    slope = 0
    intercept = 3
    xval = 5
    if hasattr(proj_functions,'create_lambda') and proj_functions.create_lambda() is not None:
        try:
            output = hashlib.sha224(str(round(
                proj_functions.create_lambda()(slope, intercept, xval),2))).hexdigest()
        except:
            output = False
    tester.run_comparison(output,
                          '1f1828e52d7ae038235abf190e8f61ed490c0e4182296ad821cdc219',
                          "The lambda function made by 'create_lambda' gives incorrect answer for slope={0},"\
                          " intercept={1}, and x-value={2}".format(slope,intercept,xval),
                          "'create_lambda' has not yet been implemented")
def test_create_lambda_rand_inputs_3():
    output = None
    slope = 1.5
    intercept = 3
    xval = -5
    if hasattr(proj_functions,'create_lambda') and proj_functions.create_lambda() is not None:
        try:
            output = hashlib.sha224(str(round(
                proj_functions.create_lambda()(slope, intercept, xval),2))).hexdigest()
        except:
            output = False
    tester.run_comparison(output,
                          '2089281d9a9b47a741c25ee15b37d2520a17ac0006d5d2ffd3c0f053',
                          "The lambda function made by 'create_lambda' gives incorrect answer for slope={0},"\
                          " intercept={1}, and x-value={2}".format(slope,intercept,xval),
                          "'create_lambda' has not yet been implemented")
def test_create_lambda_rand_inputs_4():
    output = None
    slope = 0
    intercept = 0
    xval = 0
    if hasattr(proj_functions,'create_lambda') and proj_functions.create_lambda() is not None:
        try:
            output = hashlib.sha224(str(round(
                proj_functions.create_lambda()(slope, intercept, xval),2))).hexdigest()
        except:
            output = False
    tester.run_comparison(output,
                          '81260578ba6b60dd121778b4e26ad4c8d2eb1d3ce2c8da38567dbb92',
                          "The lambda function made by 'create_lambda' gives incorrect answer for slope={0},"\
                          " intercept={1}, and x-value={2}".format(slope,intercept,xval),
                          "'create_lambda' has not yet been implemented")
    

    
