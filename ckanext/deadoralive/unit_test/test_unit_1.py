#!/usr/bin/env python2.7

import sys
import argparse
import socket

import requests
import requests.exceptions

from junitparser import TestCase,TestSuite,JUnitXml,Skipped,Error,Failure

def get_resources_to_check(client_site_url, apikey):
    
    url = client_site_url + u"deadoralive/get_resources_to_check"
    response = requests.get(url, headers=dict(Authorization=apikey))
    #.loads()
    if not response.ok:
      	 #raise CouldNotGetResourceIDsError(u"Couldn't get resource IDs to check: {code} {reason}".format(code=response.status_code, reason=response.reason))
         return False,response
    else:
         data = response.json()
         if len(data) == 50:
            return True,response
    return False,response

def get_url_for_id(client_site_url, apikey, resource_id):
    
    url = client_site_url + u"deadoralive/get_url_for_resource_id"
    params = {"resource_id": resource_id}
    response = requests.get(url, headers=dict(Authorization=apikey), params=params)
    if not response.ok:
        #raise CouldNotGetURLError(u"Couldn't get URL for resource {id}: {code} {reason}".format(id=resource_id, code=response.status_code,reason=response.reason))
        return False,response
    else:
         data = response.json()
         if not data == None:
            return True,response
    return False,response

def main(args=None):

    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--apikey", required=True, default="cdeb2184-cb23-40a1-bdfd-d0fe2715547a")
    parser.add_argument("--port", type=int, default=4723)
    parsed_args = parser.parse_args(args)
    client_site_url = parsed_args.url
    if not client_site_url.endswith("/"):
        client_site_url = client_site_url + "/"
    apikey = parsed_args.apikey
    port = parsed_args.port
    s = socket.socket()
    try:
        s.bind(('localhost', port))
    except socket.error as err:
        if err.errno == 98:
            #Create Test Cases
            case1 = TestCase('Test1')
            case1.name = 'Test for get_resources'
            case1.result = Failure('Test failed. Can not connect because port is actually used',err)
            #Create Test Suite
            suite = TestSuite('Suite1')
            suite.name = 'Test suite 1'
            suite.add_testcase(case1)
            #Add info into JunitXml
            xml = JUnitXml()
            xml.add_testsuite(suite)
            xml.write('junit_test.xml')
            sys.exit(
                "Port {port} is already in use.\n"
                "Is there another instance of {process} already running?\n"
                "To run multiple instances of {process} at once use the "
                "--port <num> option.".format(port=port, process=sys.argv[0]))
        else:
            raise
    try:
        response = requests.get(client_site_url, headers=dict(Authorization=apikey))
    except requests.exceptions.RequestException as err:
           #Create Test Cases
           case1 = TestCase('Test1')
           case1.name = 'Test the connection to client_site_url'
           case1.result = Failure('Test failed. Cannot connect to the client_site_url',err)
           #Create Test Suite
           suite = TestSuite('Suite1')
           suite.name = 'Test suite 1'
           suite.add_testcase(case1)
           #Add info into JunitXml
           xml = JUnitXml()
           xml.add_testsuite(suite)
           xml.write('junit_test.xml')
           sys.exit("The client could not connect with the client site due to {error}".format(error=err))
    success, response = get_resources_to_check(client_site_url, apikey)
    data = response.json()
    if success:
       #Create Test Cases
       case1 = TestCase('Test1')
       case1.name = 'Test for get_resources'
       case1.result = Skipped('Test passed successfully with 50 resources obtained')
    else:
       #Create Test Cases
       if not response.ok:
          case1 = TestCase('Test1')
          case1.name = 'Test for get_resources'
          case1.result = Failure('Client could not get the list with code error {0} and reason {1}'.format(response.status_code,response.reason),'failure_of_connection')
       else:
          case1 = TestCase('Test1')
          case1.name = 'Test for get_resources'
          case1.result = Error('Client could not get the list correctly, it only have got {0} resources'.format(len(data)),'error_list')
    resource_id = data[0]
    success, response = get_url_for_id(client_site_url, apikey, resource_id)
    if success:
       #Create Test Cases
       case2 = TestCase('Test2')
       case2.name = 'Test for get_url_for_resource_id'
       case2.result = Skipped('Test passed successfully with the url obtained correctly')
    else:
       #Create Test Cases
       if not response.ok:
          case2 = TestCase('Test2')
          case2.name = 'Test for get_url_for_resource_id'
          case2.result = Failure('Client could not get the url for the resource with code error {0} and reason {1}'.format(response.status_code,response.reason),'failure_of_connection')
       else:
          case2 = TestCase('Test2')
          case2.name = 'Test for get_url_for_resource_id'
          case2.result = Error('Client could not get the url correctly','the_error_type')
    #Create Test Suite
    suite = TestSuite('Suite1')
    suite.name = 'Test suite 1'
    suite.add_testcase(case1)
    suite.add_testcase(case2)
    #Add info into JunitXml
    xml = JUnitXml()
    xml.add_testsuite(suite)
    xml.write('junit_test.xml')
if __name__ == "__main__":
    main()
