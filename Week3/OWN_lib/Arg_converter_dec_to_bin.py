#!/usr/bin/env python

import sys
import IPCheck

if len(sys.argv) != 2: #выдаём ошибку, если аргументов больше одного или наоборот нет
    print('Give AN argument!')
    sys.exit()


ip_addr = sys.argv.pop()
IPCheck.IP_check(ip_addr)
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