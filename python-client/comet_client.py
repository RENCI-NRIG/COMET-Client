#!/usr/bin/env python
#
# Copyright (c) 2017 Renaissance Computing Institute, except where noted.
# All rights reserved.
#
# This software is released under GPLv2
#
# Renaissance Computing Institute,
# (A Joint Institute between the University of North Carolina at Chapel Hill,
# North Carolina State University, and Duke University)
# http://www.renci.org
#
# For questions, comments please contact software@renci.org
#
# Author: Komal Thareja(kthare10@renci.org)
import sys
import os
import time
import json
import argparse
import subprocess

from comet_common_iface import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o',
        '--operation',
        dest='operation',
        type = str,
        help='Operation allowed values: get_family|create_family|update_family|delete_family|enumerate_families|delete_families',
        required=True
    )
    parser.add_argument(
        '-c',
        '--comethost',
        dest='comethost',
        type = str,
        help='Comet Host e.g. https://13.59.255.221:8111/',
        required=True
    )
    parser.add_argument(
        '-i',
        '--inputFile',
        dest='inputFile',
        type = str,
        help='Input File',
        required=True
    )

    args = parser.parse_args()

    inputJsonTxt = open(args.inputFile).read()
    inputJson = json.loads(inputJsonTxt)

    if inputJson["contextId"] is None:
        print("Missing required field: contextId")
        parser.print_help()
        sys.exit(1)

    if args.operation == 'get_family':
        get_family(args, inputJson)
    elif args.operation == 'create_family':
        if inputJson["caCert"] is None or inputJson["cert"] is None or inputJson["certKey"] is None:
            print("CA Cert, Client Cert and Client Key is required for create_family")
            parser.print_help()
            sys.exit(1)
        create_update_family(args, inputJson)
    elif args.operation == 'update_family':
        create_update_family(args, inputJson)
    elif args.operation == 'delete_family':
        if inputJson["caCert"] is None or inputJson["cert"] is None or inputJson["certKey"] is None:
            print("CA Cert, Client Cert and Client Key is required for delete_family")
            parser.print_help()
            sys.exit(1)
        delete_family(args, inputJson)
    elif args.operation == 'enumerate_families':
        enumerate_families(args, inputJson)
    elif args.operation == 'delete_families':
        delete_families(args, inputJson)
    else:
        parser.print_help()
        sys.exit(1)

    sys.exit(0)

def get_family (args, inputJson):
    try:
        comet=CometInterface(args.comethost, inputJson["caCert"], inputJson["cert"], inputJson["certKey"])
        response=comet.get_family(args.comethost, inputJson["contextId"], inputJson["key"], inputJson["readToken"], inputJson["family"])
        print ("get_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("get_family: Received Response Message: " + response.json()["message"])
            print("get_family: Received Response Status: " + response.json()["status"])
            print("get_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def create_update_family(args, inputJson):
    try:
        comet=CometInterface(args.comethost, None, inputJson["cert"], inputJson["certKey"], None)
        response=comet.update_family(args.comethost, inputJson["contextId"], inputJson["key"],
                                     inputJson["readToken"], inputJson["writeToken"], inputJson["family"], inputJson["value"])
        print ("create_update_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("create_update_family: Received Response Message: " + response.json()["message"])
            print("create_update_family: Received Response Status: " + response.json()["status"])
            print("create_update_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def delete_family(args, inputJson):
    try:
        comet=CometInterface(args.comethost, inputJson["caCert"], inputJson["cert"], inputJson["certKey"], None)
        response=comet.delete_family(args.comethost, inputJson["contextId"], inputJson["key"],inputJson["readToken"], inputJson["writeToken"], inputJson["family"])
        print ("delete_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("delete_family: Received Response Message: " + response.json()["message"])
            print("delete_family: Received Response Status: " + response.json()["status"])
            print("delete_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def enumerate_families(args, inputJson):
    try:
        comet=CometInterface(args.comethost, inputJson["caCert"], inputJson["cert"], inputJson["certKey"])
        response=comet.enumerate_families(args.comethost, inputJson["contextId"], inputJson["readToken"], inputJson["family"])
        print ("enumerate_families: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("enumerate_families: Received Response Message: " + response.json()["message"])
            print("enumerate_families: Received Response Status: " + response.json()["status"])
            print("enumerate_families: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def delete_families(args, inputJson):
    try:
        comet=CometInterface(args.comethost, inputJson["caCert"], inputJson["cert"], inputJson["certKey"])
        response=comet.delete_families(args.comethost, inputJson["contextId"], inputJson["key"], inputJson["readToken"], inputJson["writeToken"])
        print ("delete_families: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("delete_families: Received Response Message: " + response.json()["message"])
            print("delete_families: Received Response Status: " + response.json()["status"])
            print("delete_families: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

if __name__ == '__main__':
    main()

