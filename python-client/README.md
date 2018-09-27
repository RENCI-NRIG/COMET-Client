# Description
Python based Comet client to invoke various supported Comet REST commands.

# Installation
`git clone https://github.com/RENCI-NRIG/COMET-Client.git`

`cd COMET-Client/python-client/`

You are now ready execute python client.

Pre-requisites: requires python 2.7 or above version and python requests package installed

# Usage
```
usage: comet_client.py [-h] -o OPERATION -c COMETHOST -i INPUTFILE

optional arguments:
  -h, --help            show this help message and exit 
  -o OPERATION, --operation OPERATION
                        Operation allowed values:
                        get_family|create_family|update_family|delete_family|enumerate_families|delete_families
  -c COMETHOST, --comethost COMETHOST
                        Comet Host e.g. https://13.59.255.221:8111/
  -i INPUTFILE, --inputFile INPUTFILE
                        Input File
```
# Input File
Input File is a json following containing following parameters:
## Input file for creating pubkeys context
[input1.json](./input1.json)

User is expected to update the values as needed.
```
{
    "contextId":"12346-ec9b-4958-b726-b063754a9143",
    "readToken":"361a67ac",
    "writeToken":"7b1c4d09",
    "family":"pubkeysall",
    "key":"12346-3f23-4a5a-9b9e-33f98884570b",
    "value":{"val_":"[{\"publicKey\":\"\"}]"},
    "caCert":"/Users/komalthareja/comet/DigiCertCA.crt",
    "cert":"/Users/komalthareja/comet/inno-hn_exogeni_net.pem",
    "certKey":"/Users/komalthareja/comet/inno-hn_exogeni_net.key"
}
```

## Input file for creating hostsall context
[input2.json](./input2.json)

User is expected to update the values as needed.
```
{
    "contextId":"12346-ec9b-4958-b726-b063754a9143",
    "readToken":"361a67ac",
    "writeToken":"7b1c4d09",
    "family":"hostsall",
    "key":"12346-3f23-4a5a-9b9e-33f98884570b",
    "value":{"val_":"[{\"host\":\"Node0\",\"ip\":\"\"}]"},
    "caCert":"/Users/komalthareja/comet/DigiCertCA.crt",
    "cert":"/Users/komalthareja/comet/inno-hn_exogeni_net.pem",
    "certKey":"/Users/komalthareja/comet/inno-hn_exogeni_net.key"
}
```

# Examples
## Create a context
`python3 comet_client.py -o create_family -c https://13.59.255.221:8111  -i ./input1.json`

## Update a context
`python3 comet_client.py -o update_family -c https://13.59.255.221:8111  -i ./input1.json`

## Get a context
`python3 comet_client.py -o get_family -c https://13.59.255.221:8111  -i ./input1.json`

## Delete a context
`python3 comet_client.py -o delete_family -c https://13.59.255.221:8111  -i ./input1.json`

## Enumerate a context
`python3 comet_client.py -o enumerate_families -c https://13.59.255.221:8111  -i ./input1.json`

## Delete all families of a context
`python3 comet_client.py -o delete_families -c https://13.59.255.221:8111  -i ./input1.json`

