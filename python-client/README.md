# Description
Python based Comet client to invoke various supported Comet REST commands.

# Installation
`git clone https://github.com/RENCI-NRIG/COMET-Client.git`

`cd COMET-Client/python-client/`

You are now ready execute python client.

Pre-requisites: requires python 2.7 or above version and python requests package installed

# Usage

usage: comet_client.py [-h] -o OPERATION -t COMETHOST -i CONTEXTID -r READTOKEN [-w WRITETOKEN] [-f FAMILY] [-k KEY]
                       [-v VALUE] [-a CACERT] [-c CLIENTCERT] [-p CLIENTKEY]
                       
optional arguments:
  -h, --help            show this help message and exit
  
  -o OPERATION, --operation OPERATION
                        Operation 
                        allowed values:get_family|create_family|update_family|delete_family|enumerate_families|delete_families
                        
  -t COMETHOST, --comethost COMETHOST
                        Comet Host e.g. https://13.59.255.221:8111/
                        
  -i CONTEXTID, --contextid CONTEXTID
                        Context Id e.g. guid
                        
  -r READTOKEN, --readtoken READTOKEN
                        Read Token; alphanumeric string with atleast 8 characters
                        
  -w WRITETOKEN, --writetoken WRITETOKEN
                        Write Token; alphanumeric string with atleast 8 characters; 
                        Required for create_family|update_family|delete_family|delete_families
                        
  -f FAMILY, --family FAMILY
                        Family; Optional for enumerate_families
                        
  -k KEY, --key KEY    
                        Key; Required for get_family|create_family|update_family|delete_family|delete_families
                        
  -v VALUE, --value VALUE
                        Value; Required for create_family|update_family
                        
  -a CACERT, --cacert CACERT
                        CA Certificate; Required for create_family
                        
  -c CLIENTCERT, --clientcert CLIENTCERT
                        Client Certificate; Required for create_family
                        
  -p CLIENTKEY, --clientkey CLIENTKEY
                        Client Key; Required for create_family
                      
# Examples
## Create a context
`python3.6 comet_client.py -o create_family -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -w 7b1c4d09 -f pubkeys -k aa491da3-3f23-4a5a-9b9e-33f98884570b -v {"val_":"[{\"publicKey\":\"\"}]"} -a /Users/komalthareja/comet/DigiCertCA.crt -c /Users/komalthareja/comet/inno-hn_exogeni_net.pem -p /Users/komalthareja/comet/inno-hn_exogeni_net.key`

## Update a context
`python3.6 comet_client.py -o update_family -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -w 7b1c4d09 -f pubkeys -k aa491da3-3f23-4a5a-9b9e-33f98884570b -v {"val_":"[{\"publicKey\":\"\"}]"}`

## Get a context
`python3.6 comet_client.py -o get_family -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -f pubkeys -k aa491da3-3f23-4a5a-9b9e-33f98884570b`

## Delete a context
`python3.6 comet_client.py -o delete_family -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -w 7b1c4d09 -f pubkeys -k aa491da3-3f23-4a5a-9b9e-33f98884570b -a /Users/komalthareja/comet/DigiCertCA.crt -c /Users/komalthareja/comet/inno-hn_exogeni_net.pem -p /Users/komalthareja/comet/inno-hn_exogeni_net.key`

## Enumerate a context
`python3.6 comet_client.py -o enumerate_families -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -k aa491da3-3f23-4a5a-9b9e-33f98884570b`

## Enumerate a specific family in a context
`python3.6 comet_client.py -o enumerate_families -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -k aa491da3-3f23-4a5a-9b9e-33f98884570b -f pubkeys`

## Delete all families of a context
`python3.6 comet_client.py -o delete_families -t https://13.59.255.221:8111 -i 04700364-ec9b-4958-b726-b063754a9143 -r 361a67ac -w 7b1c4d09 -f pubkeys -k aa491da3-3f23-4a5a-9b9e-33f98884570b -a /Users/komalthareja/comet/DigiCertCA.crt -c /Users/komalthareja/comet/inno-hn_exogeni_net.pem -p /Users/komalthareja/comet/inno-hn_exogeni_net.key`
