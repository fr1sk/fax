print range(0,10)

a = [(i, 2**i) for i in range(0,10)]
print a

print range(len(a))

for i in range(len(a)):
    print a[i]

'''
for x in a:
    a.insert(0,"prvo")
    print x
'''
