l = ("danas", 2, "tri", 4.55)
print l

'''l[3] = 555'''
l = list()
print l

l = list(("danas", "je", 3, "cas"))
print l
print l[1]
l[1] = "nije"
print l

l1 = [1,2,3,4,5,"duva","vetar"]
print l1
print l1[2:-1]

a=l+l1
print a
'''print a[4][2]'''
'''print a[4][5]'''
print l
print l1

a=l1[:]
print a

a.append("jedan")
print a

a.insert(0, "jedn")
print a

print a[0:0]
print a[0:1]

a[0:0] = [7.86]
print a

print a[-1:0]

a.pop()
print a
a.pop(1)
print a

a = a+[1,2,3,4,5,6]*2
print a

print a.count(1)
print a.count("vetar")

a.pop()
print a

a.remove(1)
print a
'''.remove(1) samo prvo pojavljivanje 1'''

print a.index("vetar")
print len(a)

print a[2:6]
a[2:6] = []
print a

print "dalje"
print a[a.index("vetar")+1:]
'''stampa od vetar pa nadalje'''
a[a.index("vetar")+1:] = []
print a

a.extend([1,2,3])
print a

a.sort()
print a

a.append((12,3))
print a

a.reverse()
print a


x = range(10)
y = range(-10, 20, 5)
'''od -10 do 20 stepen 5'''

print x
print y

