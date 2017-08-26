# IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
#     A. Check that the IP address contains 4 octets.
#     B. The first octet must be between 1 - 223.
#     C. The first octet cannot be 127.
#     D. The IP address cannot be in the 169.254.X.X address space.
#     E. The last three octets must range between 0 - 255.


import sys

def IP_check(ip_addr):
    class NotValidIP(Exception):
        pass

    class NotValidIPLength(Exception):
        pass

    while True:
        try:
            ip_addr_split = ip_addr.split('.') #разбиваем на октеты
            len1 = len(ip_addr_split) #записываем длину адреса в переменную
            ip_addr_split = ip_addr_split[:4] #ограничиваем четырьмя октетами
            i=0
            for element in ip_addr_split: #переводим в инт и проверяем валидность каждого октета
                ip_addr_split[i] = int(element)
                if (ip_addr_split[0] > 223 or ip_addr_split[0] < 1) or (ip_addr_split[0] == 127) or (ip_addr_split[i] > 255 or ip_addr_split[i] < 0) or (ip_addr_split[0] == 169 and ip_addr_split[1] == 254):
                    raise NotValidIP
                i +=1
            if (len1!=4):
                raise NotValidIPLength
            break
        except ValueError: #если не переводится в инт, значит значение октета неправильное
            print(ip_addr)
            print('Not a good value')
            sys.exit()
        except NotValidIP:
            print(ip_addr)
            print('this is not a valid IP address')
            sys.exit()
        except NotValidIPLength:
            print(ip_addr)
            print('this is not an IP address size')
            sys.exit()