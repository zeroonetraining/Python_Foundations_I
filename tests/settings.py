'''
This file contains configuration parameters for the tests.
All defaults are those used by Moving Data unless noted
otherwise, to help show what values each variable should take.
'''
import os

# gets the top level directory for the whole project
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#Course information:
#course_id: Course id used by our monitoring platform,
#    currently just the COU item id with 'course' instead
#    of 'ITM'
#course_repo_name: The name of the course repository
course_id = 'course_2083891'
course_repo_name = 'Python_Foundations_I'

#Test upload settings:
#upload_sentinel: If this file exists, *DON'T* upload
#    the test results. Set to this file by default,
#    so you don't accidentally upload results to our
#    server during development.
#stored_results_file: a filepath to hold queued test
#    results waiting for the student to connect to
#    visigoth before bulk uploading Should end with
#    .nogit extension to prevent git from trying to
#    add it to version control.
#ES_rooturl: The root url for elasticsearch
#ES_index: the elasticsearch index
#ES_type: the elasticsearch object type
upload_sentinel = os.path.join(PROJECT_ROOT,'tests/.donotupload.nogit')
stored_results_file = os.path.join(PROJECT_ROOT,'tests/.stored_test_results.nogit')
ES_rooturl = 'http://ilab-stackato-dev256.labs.wld.capitalone.com/'
ES_index = 'test-index-python-i'
ES_type = 'test-result'

#Note: The default index will likely change as we
#improve our platform. In fact, you can create your
#own indices willy nilly if you'd like, but you'll
#need to create the mapping for them to get the
#dates working right. Here's an example using curl:
#curl -XPOST "<ROOTURL>/<INDEX>/" -d '{"mappings":{"test-result":{"properties":{"course_slug":{"type":"string","index":"not_analyzed"},"eid":{"type":"string","index":"not_analyzed"},"project_name":{"type":"string","index":"not_analyzed"},"test_name":{"type":"string","index":"not_analyzed"},"timestamp":{"type":"date","format":"dateOptionalTime"},"value":{"type":"string","index":"not_analyzed"},"test_script":{"type":"string","index":"not_analyzed"}}}}}'
