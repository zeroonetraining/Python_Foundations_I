#Hashing the output as well as the correct answer prevents cheating
import hashlib

import numpy as np
import os

#The exercise script:
import exercises.numpy_exercises as proj_numpy
#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,stored_results_file=settings.stored_results_file,no_upload_file=settings.upload_sentinel)

def test_create_array_is_numpy_array():
    output = proj_numpy.create_array()
    is_numpy_array = None
    if output is not None:
        is_numpy_array = False
        try:
            output.shape
            is_numpy_array = True
        except:
            pass
    tester.run_comparison(is_numpy_array,
                          True,
                          "'create_array' does not return a Numpy array!"\
                          " Returns type {0} instead.".format(type(output)),
                          "'create_array' has not yet been implemented")
def test_create_array_shape():
    output = proj_numpy.create_array()
    num_dimen_output = output
    if num_dimen_output is not None:
        try:
            num_dimen_output = len(output.shape)
        except:
            num_dimen_output = "[ERROR: NOT NUMPY ARRAY]"
    tester.run_comparison(num_dimen_output,
                          1,
                          "'create_array' returns an array with the "\
                          "wrong number of dimensions! Returned array has"\
                          " {0} dimensions.".format(num_dimen_output),
                          "'create_array' has not yet been implemented")
def test_create_array_dtype():
    output = proj_numpy.create_array()
    dtype_output = output
    if dtype_output is not None:
        try:
            dtype_output = output.dtype.name
        except:
            dtype_output = "[ERROR: NOT NUMPY ARRAY]"
    tester.run_comparison(dtype_output,
                          ['int8','int16','int32','int64'],
                          "'create_array' returns an array with the "\
                          "wrong type! Got array with type {0}".format(dtype_output),
                          "'create_array' has not yet been implemented")
def test_create_array_values():
    output = proj_numpy.create_array()
    if output is not None:
        try:
            output.dtype
            #Stringify it:
            output = hashlib.sha224("".join([str(element) for element in output])).hexdigest()
        except:
            output = "[ERROR: NOT NUMPY ARRAY]"
    tester.run_comparison(output,
                          '5bd04a69c6a7bf667c7dca114eea4248b6f4117ffbb4faeb2a3caf88',
                          "'create_array' returns an array with the "\
                          "wrong values! For reference, first several elements should"\
                          " be [0, 3, 6, 9, 12, 15]",
                          "'create_array' has not yet been implemented")

def test_compute_avg_length_1d():
    input_array = np.arange(100)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          100,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 1D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
def test_compute_avg_length_1d_2():
    input_array = np.arange(1234)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          1234,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 1D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
def test_compute_avg_length_2d():
    input_array = np.arange(100).reshape(50,2)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          26,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 2D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
def test_compute_avg_length_2d_2():
    input_array = np.arange(100).reshape(10,10)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          10,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 2D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
def test_compute_avg_length_3d():
    input_array = np.random.rand(51,13,23)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          29,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 3D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
def test_compute_avg_length_3d_2():
    input_array = np.random.rand(50,28,0)
    output = proj_numpy.compute_avg_length(input_array)
    int_output = output
    if output is not None:
        try:
            int_output = int(output)
        except:
            pass
    tester.run_comparison(int_output,
                          26,
                          "'compute_avg_length' returns the wrong answer for "\
                          "a 3D array! Tried an array with shape={0},"\
                          " got {1} as output.".format(input_array.shape, output),
                          "'compute_avg_length' has not yet been implemented")
                          

def test_filter_array_all_present():
    np.random.seed(891)
    input_array = np.random.randint(0,30,15)
    output = proj_numpy.filter_array(input_array,input_array)
    tester.run_container_comparison(output,
                          input_array,
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array= {2}"\
                          .format(input_array,input_array,None),
                          "'filter_array' has not yet been implemented")
def test_filter_array_none_present():
    np.random.seed(891)
    input_array = np.random.randint(0,30,15)
    equal_array = input_array + np.random.randint(1,30,15)
    output = proj_numpy.filter_array(input_array,equal_array)
    try:
        output = len(output)
    except:
        pass
    tester.run_container_comparison(output,
                          0,
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,equal_array,None),
                          "'filter_array' has not yet been implemented")
def test_filter_array_some_present():
    np.random.seed(891)
    input_array = np.array([9,24,11,14,18,22,14,2,25,3,26,22,1,9,3])
    equal_array = np.array([9,26,9,14,15,20,16,4,23,4,23,21,2,6,3])
    output = proj_numpy.filter_array(input_array,equal_array)
    tester.run_container_comparison(output,
                          np.array([9,14,3]),
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,equal_array,None),
                          "'filter_array' has not yet been implemented")
def test_filter_array_all_present_all_not_present():
    np.random.seed(891)
    input_array = np.random.randint(0,30,15)
    not_equal_array = input_array + 9
    output = proj_numpy.filter_array(input_array,input_array,
                                     not_equal_array=not_equal_array)
    tester.run_container_comparison(output,
                          input_array,
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,input_array,not_equal_array),
                          "'filter_array' has not yet been implemented")
def test_filter_array_all_not_present_all_not_present():
    np.random.seed(891)
    input_array = np.random.randint(0,30,15)
    equal_array = input_array + 3
    not_equal_array = input_array + 9
    output = proj_numpy.filter_array(input_array,equal_array,
                                     not_equal_array=not_equal_array)
    try:
        output = len(output)
    except:
        pass
    tester.run_container_comparison(output,
                          0,
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,equal_array,not_equal_array),
                          "'filter_array' has not yet been implemented")
def test_filter_array_all_present_some_not_present():
    np.random.seed(891)
    input_array = np.random.randint(0,30,15)
    equal_array = input_array
    not_equal_array = input_array + 9
    not_equal_array[3::4] = input_array[3::4]
    output = proj_numpy.filter_array(input_array,equal_array,
                                     not_equal_array=not_equal_array)
    tester.run_container_comparison(output,
                          input_array[(input_array != not_equal_array)],
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,equal_array,not_equal_array),
                          "'filter_array' has not yet been implemented")
def test_filter_array_some_present_some_not_present():
    np.random.seed(891)
    input_array =     np.array([9,24,11,14,18,22,14,2,25,3,26,22,1,9,3])
    equal_array =     np.array([9,18,17,14,17,22,40,3,27,0,26,22,32,43,12])
    not_equal_array = np.array([7,27,11,16,18,25,10,2,13,0,26,27,0,9,12])
    output = proj_numpy.filter_array(input_array,equal_array,
                                     not_equal_array=not_equal_array)
    tester.run_container_comparison(output,
                          np.array([9,14,22,22]),
                          "'filter_array' returns the wrong answer for "\
                          "an array! Tried with these inputs:\narray_to_filter"\
                          " ={0}\nequal_array     ={1}\nnot_equal_array ={2}"\
                          .format(input_array,equal_array,not_equal_array),
                          "'filter_array' has not yet been implemented")
    

def test_reverse_multiply_zero():
    input_array = np.zeros(10)
    output = proj_numpy.reverse_multiply(input_array)
    tester.run_container_comparison(output,
                            input_array,
                            "'reverse_multiply' returns the wrong answer for "\
                            "an array! Tried with this array:\ninput_array"\
                            " ={0}".format(input_array),
                            "'reverse_multiply' has not yet been implemented")
def test_reverse_multiply_middle_1():
    input_array = np.zeros(9)
    input_array[4] = 1
    output = proj_numpy.reverse_multiply(input_array)
    tester.run_container_comparison(output,
                            input_array,
                            "'reverse_multiply' returns the wrong answer for "\
                            "an array! Tried with this array:\ninput_array"\
                            " ={0}".format(input_array),
                            "'reverse_multiply' has not yet been implemented")
def test_reverse_multiply_range():
    input_array = np.arange(10)
    output = proj_numpy.reverse_multiply(input_array)
    tester.run_container_comparison(output,
                            input_array*np.arange(9,-1,-1),
                            "'reverse_multiply' returns the wrong answer for "\
                            "an array! Tried with this array:\ninput_array"\
                            " ={0}".format(input_array),
                            "'reverse_multiply' has not yet been implemented")
def test_reverse_multiply_negative_range():
    input_array = np.arange(10)*-1
    output = proj_numpy.reverse_multiply(input_array)
    tester.run_container_comparison(output,
                            input_array*np.arange(9,-1,-1)*-1,
                            "'reverse_multiply' returns the wrong answer for "\
                            "an array! Tried with this array:\ninput_array"\
                            " ={0}".format(input_array),
                            "'reverse_multiply' has not yet been implemented")
    
def test_compute_set_intersection_unique():
    array_1 = np.arange(11)
    array_2 = np.arange(6,20)
    output = proj_numpy.compute_set_intersection(array_1,array_2)
    if output is not None:
        try:
            output = np.sort(output)
        except:
            pass
    tester.run_container_comparison(output,
                            np.array([6,7,8,9,10]),
                            "'compute_set_intersection' returns the wrong answer "\
                            "! Tried with these inputs:\narray_1"\
                            " ={0}\narray_2 ={1}".format(array_1,array_2),
                            "'compute_set_intersection' has not yet been implemented")
def test_compute_set_intersection_nonunique():
    array_1 = np.arange(10)
    array_1 = np.append(array_1,array_1)
    array_2 = np.arange(4,8)
    array_2 = np.append(array_2,array_2)
    output = proj_numpy.compute_set_intersection(array_1,array_2)
    if output is not None:
        try:
            output = np.sort(output)
        except:
            pass
    tester.run_container_comparison(output,
                            np.array([4,5,6,7]),
                            "'compute_set_intersection' returns the wrong answer "\
                            "! Tried with these inputs:\narray_1"\
                            " ={0}\narray_2 ={1}".format(array_1,array_2),
                            "'compute_set_intersection' has not yet been implemented")
def test_compute_set_intersection_none():
    array_1 = np.arange(20,30)
    array_1 = np.append(array_1,array_1)
    array_2 = np.arange(10,19)
    array_2 = np.append(array_2,array_2)
    output = proj_numpy.compute_set_intersection(array_1,array_2)
    if output is not None:
        try:
            output = np.sort(output)
        except:
            pass
    tester.run_container_comparison(output,
                            np.array([]),
                            "'compute_set_intersection' returns the wrong answer "\
                            "! Tried with these inputs:\narray_1"\
                            " ={0}\narray_2 ={1}".format(array_1,array_2),
                            "'compute_set_intersection' has not yet been implemented")

def test_save_multiple_medians_1():
    input_array = np.arange(30).reshape(10,3)
    filename = ".test_output.nogit"
    try:
        os.remove(filename)
    except:
        pass
    proj_numpy.save_multiple_medians(input_array, filename)
    output = None
    try:
        output_arr = np.loadtxt(filename,ndmin=1).astype(np.int)
        output = hashlib.sha224("".join([str(element) for element in output_arr])).hexdigest()
    except:
        pass
    try:
        os.remove(filename)
    except:
        pass
    tester.run_container_comparison(output,
                                    '93a23dff7ac5dd7ae4a627335380e09cbb4c71660849b8535ba9ee31',
                                    "'save_multiple_medians' saves the wrong answer!"\
                                    " Tried with this array:\ninput_array"\
                                    " ={0}".format(input_array),
                                    "'save_multiple_medians' has not yet been implemented or has an error that prevents this test from executing properly.")
def test_save_multiple_medians_2():
    input_array = np.arange(310).reshape(10,31)
    filename = ".test_output.nogit"
    try:
        os.remove(filename)
    except:
        pass
    proj_numpy.save_multiple_medians(input_array, filename)
    output = None
    try:
        output_arr = np.loadtxt(filename, ndmin=1).astype(np.int)
        output = hashlib.sha224("".join([str(element) for element in output_arr])).hexdigest()
    except:
        pass
    try:
        os.remove(filename)
    except:
        pass
    tester.run_container_comparison(output,
                                    '5a123fb9696675c1d0a763bc8bab89cd3dc640d9e7a3338cf0582305',
                                    "'save_multiple_medians' saves the wrong answer!"\
                                    " Tried with an array created with this command: "\
                                    "'np.arange(310).reshape(10,31)'",
                                    "'save_multiple_medians' has not yet been implemented or has an error that prevents this test from executing properly.")
