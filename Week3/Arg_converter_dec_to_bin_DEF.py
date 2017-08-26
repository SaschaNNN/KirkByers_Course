#!/usr/bin/env python

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

if len(sys.argv) != 2: #выдаём ошибку, если аргументов больше одного или наоборот нет
    print('Give AN argument!')
    sys.exit()


ip_addr = sys.argv.pop()
IP_check(ip_addr)
octets = ip_addr.split('.')

i=0
for element in octets:
    octets[i] = bin(int(element)) #бинаризируем
    octets[i] = str(octets[i]) #переводим в строку, чтобы отбросить "0b"
    octets[i] = octets[i][2:] #отбрасываем "0b"
    while len(octets[i]) < 8: #пока длина элемента не 8
        octets[i] = '0' + octets[i] #добавляем 0
    i+=1


a_joined = '.'.join(octets)

print('%-20s %26s' % ('IP ADDRESS', 'BINARY IP ADDRESS'))
print('%-20s %26s' % (ip_addr, a_joined))