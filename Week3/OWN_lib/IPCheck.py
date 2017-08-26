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
                if (ip_addr_split[i] > 255 or ip_addr_split[i] < 0):
                    raise NotValidIP
                i +=1
            if (len1!=4):
                raise NotValidIPLength
            break
        except ValueError: #если не переводится в инт, значит значение октета неправильное
            print('Not a good value')
            sys.exit()
        except NotValidIP:
            print('this is not a valid IP address')
            sys.exit()
        except NotValidIPLength:
            print('this is not an IP address size')
            sys.exit()