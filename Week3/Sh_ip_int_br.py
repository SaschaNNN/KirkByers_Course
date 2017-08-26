#!/usr/bin/env python

show_ip_int_brief = '''
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
'''

a = show_ip_int_brief.strip()
brief = a.split('\n')

i=0
for element in brief:
    line = element.split()
    inter, ip, ok, method, status, proto = line
    if inter == 'Interface':
        print(brief[i])
    if status == 'up' and proto == 'up':
        print(brief[i])
    i+=1


