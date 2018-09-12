# Usage

usage: comet_client.py [-h] -o OPERATION -t COMETHOST -i CONTEXTID -r
                       READTOKEN [-w WRITETOKEN] [-f FAMILY] [-k KEY]
                       [-v VALUE] [-a CACERT] [-c CLIENTCERT] [-p CLIENTKEY]
                       

optional arguments:

  -h, --help            show this help message and exit
  
  -o OPERATION, --operation OPERATION
                        Operation get_family|create_family|update_family|delete_family|enumerate_families|delete_families
                        
  -t COMETHOST, --comethost COMETHOST
                        Comet Host
                        
  -i CONTEXTID, --contextid CONTEXTID
                        Context Id
                        
  -r READTOKEN, --readtoken READTOKEN
                        Read Token
                        
  -w WRITETOKEN, --writetoken WRITETOKEN
                        Write Token, required for [create_family, update_family, delete_family, delete_families]
                        
  -f FAMILY, --family FAMILY
                        Family, optional for [enumerate_families]
                        
  -k KEY, --key KEY     Key, required for [get_family, create_family, update_family, delete_family, delete_families]
  
  -v VALUE, --value VALUE
                        Value, required for [create_family, update_family]
                        
  -a CACERT, --cacert CACERT
                        CA Certificate, required for operation=create_family
                        
  -c CLIENTCERT, --clientcert CLIENTCERT
                        Client Certificate, required for operation=create_family
                        
  -p CLIENTKEY, --clientkey CLIENTKEY
                        Client Key, required for operation=create_family
                        
