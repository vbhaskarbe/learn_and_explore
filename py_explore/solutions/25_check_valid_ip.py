#
## 25. Check for valid IPV4 IP address in given string
#

import re

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def check_ipv4(Ip):
    if(re.search(regex, Ip)):  
        print("%15s is Valid Ip4 address." % Ip)  
    else:  
        print("%15s is Invalid Ip4 address." % Ip)

if __name__ == '__main__' :
    Ip = "192.168.0.1"
    check_ipv4(Ip)

    Ip = "110.234.52.124"
    check_ipv4(Ip)

    Ip = "366.1.2.2"
    check_ipv4(Ip)

