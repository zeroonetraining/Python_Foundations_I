#Hashing the output as well as the correct answer prevents cheating
import hashlib

import os
import sys
import time
# from StringIO import StringIO

#The exercise script:
import exercises.read_and_write as rw
#The testing function library:
import testing_functions as tf
#Configuration parameters:
import settings

tester = tf.TestClass(settings.course_id,settings.course_repo_name,stored_results_file=settings.stored_results_file,no_upload_file=settings.upload_sentinel)

class TestReadWrite(object):
    def test_read_csv_seenfile(self):
        test_file = os.path.join(os.path.join(settings.PROJECT_ROOT, 'data'), 'old_transactions.csv')
        output = rw.read_csv(test_file)
        if output is not None:
            output = hashlib.sha224(str(output)).hexdigest()
        correct_output = '958d42a83cf840cde79922f0795fd6ac7da4d2df828edc32244bb3ba'
        tester.run_comparison(output, correct_output,
                              "'read_csv' gives an incorrect result for"\
                              " the file {0}.".format(test_file),
                              "'read_csv' has not yet been implemented")
    def test_read_csv_unseenfile(self):
        test_file = os.path.join(os.path.join(settings.PROJECT_ROOT, 'data'), 'test_old_file.csv')
        output = rw.read_csv(test_file)
        if output is not None:
            output = hashlib.sha224(str(output)).hexdigest()
        correct_output = '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'
        tester.run_comparison(output, correct_output,
                              "'read_csv' gives an incorrect result for"\
                              " the file {0}.".format(test_file),
                              "'read_csv' has not yet been implemented")

    def test_read_json_seenfile(self):
        test_file = os.path.join(os.path.join(settings.PROJECT_ROOT, 'data'), 'new_transactions.json')
        output = rw.read_json(test_file)
        if output is not None:
            output = hashlib.sha224(str(output)).hexdigest()
        correct_output = '76697f0422973db5da706211f8558aee92183497146be1fbca9abcd8'
        tester.run_comparison(output, correct_output,
                              "'read_json' gives an incorrect result for"\
                              " the file {0}.".format(test_file),
                              "'read_json' has not yet been implemented")
    def test_read_json_unseenfile(self):
        test_file = os.path.join(os.path.join(settings.PROJECT_ROOT, 'data'), 'test_json_file.json')
        output = rw.read_json(test_file)
        if output is not None:
            output = hashlib.sha224(str(output)).hexdigest()
        correct_output = '4b4372e1eba8674b79f28229402dd9d97da384466d78e9833962ce5d'
        tester.run_comparison(output, correct_output,
                              "'read_json' gives an incorrect result for"\
                              " the file {0}.".format(test_file),
                              "'read_json' has not yet been implemented")

    def test_write_csv_1(self):
        test_file = '.test.csv.nogit'
        test_data = [[1,2,3],[4,5,6],[7,8,9]]
        correct_output = ["1,2,3\n4,5,6\n7,8,9\n", "1,2,3\n4,5,6\n7,8,9",
                          "1,2,3\r\n4,5,6\r\n7,8,9\r\n", "1,2,3\r\n4,5,6\r\n7,8,9",
                          "1,2,3\r4,5,6\r7,8,9\r", "1,2,3\r4,5,6\r7,8,9"]
        curr_time = int(time.time())
        rw.write_csv(test_data,test_file)
        output = None
        if os.path.isfile(test_file):
            if os.stat(test_file).st_mtime >= curr_time:
                with open(test_file,'r') as handle:
                    output = "".join(handle.readlines())
            os.remove(test_file)
                    
        tester.run_comparison(output,correct_output,
                              "'write_csv' gives an incorrect result for"\
                              "'data_list' = {0}".format(test_data),
                              "'write_csv' has not yet been implemented")

    def test_write_csv_2(self):
        test_file = '.test.csv.nogit'
        test_data = [["hi","my","name"],["is","Lee","Cardholder"],["and","I","am"],[30,"years","old"]]
        correct_output = ["hi,my,name\nis,Lee,Cardholder\nand,I,am\n30,years,old\n",
                           "hi,my,name\nis,Lee,Cardholder\nand,I,am\n30,years,old",
                           "hi,my,name\r\nis,Lee,Cardholder\r\nand,I,am\r\n30,years,old\r\n",
                           "hi,my,name\r\nis,Lee,Cardholder\r\nand,I,am\r\n30,years,old",
                           "hi,my,name\ris,Lee,Cardholder\rand,I,am\r30,years,old\r",
                           "hi,my,name\ris,Lee,Cardholder\rand,I,am\r30,years,old"]
        curr_time = int(time.time())
        rw.write_csv(test_data,test_file)
        output = None
        if os.path.isfile(test_file):
            if os.stat(test_file).st_mtime >= curr_time:
                with open(test_file,'r') as handle:
                    output = "".join(handle.readlines())
            os.remove(test_file)
        tester.run_comparison(output,correct_output,
                              "'write_csv' gives an incorrect result for"\
                              "data_list = {0}".format(test_data),
                              "'write_csv' has not yet been implemented")


