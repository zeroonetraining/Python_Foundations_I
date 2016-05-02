#Hashing the output as well as the correct answer prevents cheating
import hashlib

#The exercise script:
import exercises.datatypes as dt
#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,stored_results_file=settings.stored_results_file,no_upload_file=settings.upload_sentinel)

class TestListProblems(object):
    def test_first_list(self):
        output = None
        if hasattr(dt,'maybe_your_first_list'):
            output = dt.maybe_your_first_list
        tester.run_container_comparison(output,[1,2,3,4,5],
                              "Incorrect values in 'maybe_your_first_list'!",
                              "'maybe_your_first_list' has not yet been created")

    def test_fibo_last(self):
        output = None
        correct_output = '95e045588bf4797d58ca899e68014e012f0710affe8bae9b9318c585'
        if hasattr(dt,'fibolist_last') and dt.fibolist_last is not None:
            output = hashlib.sha224(str(dt.fibolist_last)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'fibolist_last'!",
                              "'fibolist_last' has not yet been assigned a value.")
        

    def test_fibo_even_entries_sum(self):
        output = None
        correct_output = '95e045588bf4797d58ca899e68014e012f0710affe8bae9b9318c585'
        if hasattr(dt,'fibolist_even_entries_sum') and dt.fibolist_even_entries_sum is not None:
            output = hashlib.sha224(str(dt.fibolist_even_entries_sum)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'fibolist_even_entries_sum'!",
                              "'fibolist_even_entries_sum' has not yet been assigned a value.")
        
    def test_fibo_add_number(self):
        output = None
        if hasattr(dt,'fibolist'):
            if len(dt.fibolist) > 50:
                output = False
                if dt.fibolist[-1] == 20365011074:
                    output = True

        tester.run_comparison(output,True,
                              "Incorrect number appended to 'fibolist'!",
                              "'fibolist' has not had the next number appended to it yet.")

    def test_fibo_reversed(self):
        output = None
        correct_output = ['fa84b857aee2308bbbbbc72b59b04db6d08e4e05c4c11b8f08c0a97e',
                          'b54b8c0152777908c489e6e53fd67b29d19d7e04817b98987df00dbc',
                          '8d8251a755d7e31a399dac45b229446276015af1e0bf8d7ff1f7f7f6',
                          '798e88305c29b863ea49d897e24d81e0ddaf390ecb620ca7eac4a31d']#Passes regardless whether 51st number has been added to list, and regardless of whether computer is 64 or 32 bit.
        if hasattr(dt,'fibolist_reversed') and dt.fibolist_reversed is not None:
            output = hashlib.sha224(str(dt.fibolist_reversed)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'fibolist_reversed'!",
                              "'fibolist_reversed' has not yet been assigned a value.")
        
    def test_list_concatenation(self):
        output = None
        correct_output = 'a032a2eca11de73cd9ee2010020db157f5d2f1e119473f989b7974af'
        if hasattr(dt,'A_and_B') and dt.A_and_B is not None:
            output = hashlib.sha224(str(dt.A_and_B)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'A_and_B'!",
                              "'A_and_B' has not yet been assigned a value.")
        
    def test_in_list(self):
        output = None
        correct_output = '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'
        if hasattr(dt,'is_1337_fibo') and dt.is_1337_fibo is not None:
            output = hashlib.sha224(str(dt.is_1337_fibo)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'is_1337_fibo'! If you're desperate, you"\
                              " should be able to look up the values of the fibonacci sequence"\
                              " to get the right answer (a boolean True/False).",
                              "'is_1337_fibo' has not yet been assigned a value.")
        

class TestTupleProblems(object):
    
    def test_first_tuple(self):
        output = None
        if hasattr(dt,'maybe_your_first_tuple'):
            output = dt.maybe_your_first_tuple
        tester.run_container_comparison(output,(0, 1, 2, 3, "hello", 4, 5, 6, 7, 8, 9, 10, 1, 4, 1, 1, 91),
                              "Incorrect values in 'maybe_your_first_tuple'!",
                              "'maybe_your_first_tuple' has not yet been created")
    def test_tuple_evens(self):
        output = None
        correct_output = 'fb1d04a0b00bf3a3e80cdf15271c1f6bf10799419fcd9e6171abc724'
        if hasattr(dt,'your_first_tuple_evens') and dt.your_first_tuple_evens is not None:
            output = hashlib.sha224(str(dt.your_first_tuple_evens)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'your_first_tuple_evens'! Remember that even "\
                              "indices are 0,2,4,6,...",
                              "'your_first_tuple_evens' has not yet been assigned a value.")
    def test_tuple_odds(self):
        output = None
        correct_output = '78262d495aa2ad4268f6248a51b5b35208e108fa8ed8170d9f6e558c'
        if hasattr(dt,'your_first_tuple_odds') and dt.your_first_tuple_odds is not None:
            output = hashlib.sha224(str(dt.your_first_tuple_odds)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'your_first_tuple_odds'! Remember that odd "\
                              "indices are 1,3,5,7,...",
                              "'your_first_tuple_odds' has not yet been assigned a value.")


class TestSetProblems(object):
    
    def test_first_set(self):
        output = None
        if hasattr(dt,'maybe_your_first_set'):
            output = dt.maybe_your_first_set
        tester.run_container_comparison(output,set([1,2,3,4]),
                              "Incorrect values in 'maybe_your_first_set'!",
                              "'maybe_your_first_set' has not yet been created")
    

    def test_distinct_elements(self):
        output = None
        correct_output = '1d7714402a19f2d20f2f910438f8e4a0910788da9494036321f99ce1'
        if hasattr(dt,'distinct_elements') and dt.distinct_elements is not None:
            output = hashlib.sha224(str(dt.distinct_elements)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'distinct_elements'! Remember to make"\
                              "'distinct_elements' into a set, not a list.",
                              "'distinct_elements' has not yet been assigned a value.")


    def test_union(self):
        output = None
        correct_output = 'f896f1b90eae2782ef0e6d2c2e5f541443089e0a419eca6fff8a9e86'
        if hasattr(dt,'A_union_B') and dt.A_union_B is not None:
            output = hashlib.sha224(str(dt.A_union_B)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'A_union_B'!",
                              "'A_union_B' has not yet been assigned a value.")

    def test_intersection(self):
        output = None
        correct_output = 'c4ffa89df9476bb1f26af29b0b9909c5680b71be0718453017d7186b'
        if hasattr(dt,'A_intersection_B') and dt.A_intersection_B is not None:
            output = hashlib.sha224(str(dt.A_intersection_B)).hexdigest()
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'A_intersection_B'!",
                              "'A_intersection_B' has not yet been assigned a value.")

class TestDictionaryProblems(object):
    
    def test_first_dict(self):
        output = None
        if hasattr(dt,'maybe_your_first_dict'):
            output = dt.maybe_your_first_dict
        tester.run_container_comparison(output,{'key1':'val1', 'key2': 'val2', 
                                 'key3': 0, 'key4': [1,2,3], (1,2):'tuples can be keys',
                                 'but not lists': ["how", "sad", "for", "lists"]},
                              "Incorrect values in 'maybe_your_first_dict'!",
                              "'maybe_your_first_dict' has not yet been created")
        
    def test_fetch(self):
        output = None
        correct_output = '04b0807efc0a69357f0a0a742ef8653dda3b97b5b1bfd132bc8a40fa'
        if hasattr(dt,'hello_there_value') and dt.hello_there_value is not None:
            output = dt.hello_there_value
        tester.run_comparison(output,correct_output,
                              "Incorrect value for 'hello_there_value'! Remember that dictionary"\
                              " values are accessed by key, unlike sets, tuples, or lists.",
                              "'hello_there_value' has not yet been assigned a value.")

    def test_delete(self):
        output = None
        if hasattr(dt,'demodict1') and dt.demodict1 is not None:
            output = False
            if len(dt.demodict1) == 5 and "there" in dt.demodict1:
                output = None
            if "there" not in dt.demodict1:
                output = True
        tester.run_comparison(output,True,
                              "'there' key not properly removed from 'demodict1'!",
                              "'demodict1' has not yet been modified.")


