#!/usr/bin/env python
import fileinput

class NotValidIP(Exception):
    pass

class NotValidIPLength(Exception):
    pass

while True:
    try:
        ip_addr = input("Enter a network IP address: ")
        ip_addr_split = ip_addr.split('.')
        len1 = len(ip_addr_split)
        ip_addr_split = ip_addr_split[:3]
        ip_addr_split.append('0')
        i=0
        for element in ip_addr_split:
            ip_addr_split[i] = int(element)
            i = i+1
        i = 0
        for element in ip_addr_split:
            if (element > 255 or element < 0):
                raise NotValidIP
        if (len1!=3 and len1!=4):
            raise NotValidIPLength
        a = '.'.join(str(q) for q in ip_addr_split)
        print("The network IP address now is: %s" % a)
        break
    except ValueError:
        print('Not a good value')
    except NotValidIP:
        print('this is not a valid IP address')
    except NotValidIPLength:
        print('this is not an IP address size')