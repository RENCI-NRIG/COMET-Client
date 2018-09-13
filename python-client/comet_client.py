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
        '-t',
        '--comethost',
        dest='comethost',
        type = str,
        help='Comet Host e.g. https://13.59.255.221:8111/',
        required=True
    )

    parser.add_argument(
        '-i',
        '--contextid',
        dest='contextid',
        type = str,
        help='Context Id e.g. guid',
        required=True
    )
    parser.add_argument(
        '-r',
        '--readtoken',
        dest='readtoken',
        type = str,
        help='Read Token; alphanumeric string with atleast 8 characters',
        required=True
    )
    parser.add_argument(
        '-w',
        '--writetoken',
        dest='writetoken',
        type = str,
        help='Write Token; alphanumeric string with atleast 8 characters; Required for create_family|update_family| delete_family|delete_families'
    )
    parser.add_argument(
        '-f',
        '--family',
        dest='family',
        type = str,
        help='Family; Optional for enumerate_families'
    )
    parser.add_argument(
        '-k',
        '--key',
        dest='key',
        type = str,
        help='Key; Required for get_family|create_family|update_family|delete_family|delete_families'
    )
    parser.add_argument(
        '-v',
        '--value',
        dest='value',
        type = str,
        help='Value; Required for create_family|update_family'
    )
    parser.add_argument(
        '-a',
        '--cacert',
        dest='cacert',
        type = str,
        help='CA Certificate; Required for create_family'
    )

    parser.add_argument(
        '-c',
        '--clientcert',
        dest='clientcert',
        type = str,
        help='Client Certificate; Required for create_family'
    )

    parser.add_argument(
        '-p',
        '--clientkey',
        dest='clientkey',
        type = str,
        help='Client Key; Required for create_family'
    )

    args = parser.parse_args()

    if args.operation != 'enumerate_families' and args.operation != 'delete_families' and args.family is None:
        print("Family is required for all operations except enumerate_families and delete_families")
        parser.print_help()
        sys.exit(1)

    if args.operation != 'enumerate_families' and args.operation != 'delete_families' and args.key is None:
        print("Key is required for all operations except enumerate_families and delete_families")
        parser.print_help()
        sys.exit(1)

    if args.operation != 'create_family' and args.operation != 'update_family' and args.value is not None:
        print("Value is required only for operations create_family and update_family")
        parser.print_help()
        sys.exit(1)

    if (args.operation == 'create_family' or args.operation == 'update_family') and args.value is None:
        print("Value and Write Token is required for operations create_family and update_family")
        parser.print_help()
        sys.exit(1)

    if args.operation != 'enumerate_families' and args.operation != 'get_family' and args.writetoken is None:
        print("Write token is required for all operations except enumerate_families and get_family")
        parser.print_help()
        sys.exit(1)

    if args.operation == 'get_family':
        get_family(args)
    elif args.operation == 'create_family':
        if args.cacert is None or args.clientcert is None or args.clientkey is None:
            print("CA Cert, Client Cert and Client Key is required for create_family")
            parser.print_help()
            sys.exit(1)
        create_update_family(args)
    elif args.operation == 'update_family':
        create_update_family(args)
    elif args.operation == 'delete_family':
        delete_family(args)
    elif args.operation == 'enumerate_families':
        enumerate_families(args)
    elif args.operation == 'delete_families':
        delete_families(args)
    else:
        parser.print_help()
        sys.exit(1)

    sys.exit(0)

def get_family (args):
    try:
        comet=CometInterface(args.comethost, args.cacert, args.clientcert, args.clientkey, None)
        response=comet.get_family(args.comethost, args.contextid, args.key, args.readtoken, args.family)
        print ("get_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("get_family: Received Response Message: " + response.json()["message"])
            print("get_family: Received Response Status: " + response.json()["status"])
            print("get_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def create_update_family(args):
    try:
        comet=CometInterface(args.comethost, args.cacert, args.clientcert, args.clientkey, None)
        response=comet.update_family(args.comethost, args.contextid, args.key, args.readtoken, args.writetoken, args.family, args.value)
        print ("create_update_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("create_update_family: Received Response Message: " + response.json()["message"])
            print("create_update_family: Received Response Status: " + response.json()["status"])
            print("create_update_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def delete_family(args):
    try:
        comet=CometInterface(args.comethost, args.cacert, args.clientcert, args.clientkey, None)
        response=comet.delete_family(args.comethost, args.contextid, args.key, args.readtoken, args.writetoken, args.family)
        print ("delete_family: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("delete_family: Received Response Message: " + response.json()["message"])
            print("delete_family: Received Response Status: " + response.json()["status"])
            print("delete_family: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def enumerate_families(args):
    try:
        comet=CometInterface(args.comethost, args.cacert, args.clientcert, args.clientkey, None)
        response=comet.enumerate_families(args.comethost, args.contextid, args.readtoken, args.family)
        print ("enumerate_families: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("enumerate_families: Received Response Message: " + response.json()["message"])
            print("enumerate_families: Received Response Status: " + response.json()["status"])
            print("enumerate_families: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

def delete_families(args):
    try:
        comet=CometInterface(args.comethost, args.cacert, args.clientcert, args.clientkey, None)
        response=comet.delete_families(args.comethost, args.contextid, args.key, args.readtoken, args.writetoken)
        print ("delete_families: Received Response Status Code=" + str(response.status_code))
        if response.json() :
            print("delete_families: Received Response Message: " + response.json()["message"])
            print("delete_families: Received Response Status: " + response.json()["status"])
            print("delete_families: Received Response Value: " + json.dumps((response.json()["value"])))
    except Exception as e:
        print("Exception occurred: " + str(type(e)) + " : " + str(e) + "\n")

if __name__ == '__main__':
    main()

