cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

a = cisco_ios.split()

print(a)

b = a.index('Version')
c = a[b+1]
d = c[:-1]
print(d)

# for i in a:
#     if i=='Version':
#         print(i)