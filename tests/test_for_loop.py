#Hashing the output as well as the correct answer prevents cheating
import hashlib

#The exercise script:
import exercises.for_loop as proj_for

#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,
                      stored_results_file=settings.stored_results_file,
                      no_upload_file=settings.upload_sentinel)

def test_total_balance():
    hashed_answer = 'a678fd9cee0991a1214d757166fb0565543ef9485ab17243d82a1d37'
    output_balance = None
    if hasattr(proj_for,'total_balance') and proj_for.total_balance is not None:
        output_balance = hashlib.sha224(str(proj_for.total_balance)).hexdigest()
    tester.run_comparison(output_balance,hashed_answer,
                          'The total_balance variable is incorrect. Try again - it should be around 250.',
                          'total_balance has not been set yet.')

def test_total_credit_balance():
    hashed_answer = '40cd73fb46d93d07a233aa344ddd91fbd8258a8dd00d30b93322e52f'
    output_credit_balance = None
    if hasattr(proj_for,'total_credit_balance') and proj_for.total_credit_balance is not None:
        output_credit_balance = hashlib.sha224(str(proj_for.total_credit_balance)).hexdigest()
    tester.run_comparison(output_credit_balance,hashed_answer,
                          'The total_credit_balance variable is incorrect. Try again - it should be around 25000.',
                          'total_credit_balance has not been set yet.')

def test_num_accounts_with_credit():
    hashed_answer = '76b8d44676fed57eb0e3627eff69165c9ea9788ad0e832560d48a146'
    output_num_accounts_with_credit = None
    if hasattr(proj_for,'num_accounts_with_credit') and proj_for.num_accounts_with_credit is not None:
        output_num_accounts_with_credit = hashlib.sha224(str(proj_for.num_accounts_with_credit)).hexdigest()
    tester.run_comparison(output_num_accounts_with_credit,hashed_answer,
                          'The num_accounts_with_credit variable is incorrect. Try again - check the boilerplate code that generated the balances and note that the random balances are uniformly distributed to get a sense of what the answer should be.',
                          'num_accounts_with_credit has not been set yet.')

def test_account_id_debt_list():
    hashed_answer = 'd6f9eaac761f15e5cc886fc7742ecdd8b77f59d59a7dfbbfb7047bbc'
    output_account_id_debt_list = None
    if hasattr(proj_for,'account_id_debt_list') and proj_for.account_id_debt_list is not None:
        account_id_debt_list = proj_for.account_id_debt_list
        output_account_id_debt_list = hashlib.sha224(''.join([str(id) for id in account_id_debt_list])).hexdigest()
    tester.run_comparison(output_account_id_debt_list,hashed_answer,
                          'The account_id_debt_list list is incorrect. Hint: the first 10 items in this list are [2,6,7,8,11,13,14,16,17,18].',
                          'account_id_debt_list has not been set yet.')

def test_account_balance_list():
    hashed_answer = '6c8ac67af3bc2f229f2b1b22eac0cccfe52456daaab6da421423961e'
    output_account_balance_list = None
    if hasattr(proj_for,'account_balance_list') and proj_for.account_balance_list is not None:
        account_balance_list = proj_for.account_balance_list
        output_account_balance_list = hashlib.sha224(''.join([str(bal) for bal in account_balance_list])).hexdigest()
    tester.run_comparison(output_account_balance_list,hashed_answer,
                          'The account_balance_list list is incorrect. Hint: the first 10 items in this list are [1983, 0, 113, 1078, 1667, 0, 0, 0, 417, 267].',
                          'account_balance_list has not been set yet.')
