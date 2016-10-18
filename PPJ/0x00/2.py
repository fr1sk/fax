l = range(10)
print l

A = set('abrakadabra')
print A

B = set([2,1,4,5,6])
print B

s = set("hokuspokus")
print A
print s


print A|s
print A.union(s)

print A&s
print A.intersection(s)


print A^s
print A.symmetric_difference(s)

'''a bez s'''
print A-s
print A.difference(s)