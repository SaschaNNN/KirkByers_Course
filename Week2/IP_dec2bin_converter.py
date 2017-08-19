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
        ip_addr_split = ip_addr_split[:4]
        i=0
        for element in ip_addr_split:
            ip_addr_split[i] = int(element)
            i = i+1 
        i = 0
        for element in ip_addr_split:
            if (element > 255 or element < 0):
                raise NotValidIP
        if (len1!=4):
            raise NotValidIPLength
        print("The network IP address now is: %s" % ip_addr_split)
        break
    except ValueError:
        print('Not a good value')
    except NotValidIP:
        print('this is not a valid IP address')
    except NotValidIPLength:
        print('this is not an IP address size')

print('%20s %20s %20s %20s' % ('FIRST_OCTET', 'SECOND_OCTET', 'THIRD_OCTET', 'FORTH_OCTET') )
a = bin(ip_addr_split[0])
b = bin(ip_addr_split[1])
c = bin(ip_addr_split[2])
d = bin(ip_addr_split[3])
print('%20s %20s %20s %20s' % (a, b, c, d))