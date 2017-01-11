lokal = dict([(123,"pera"),(234, "sava")])
lokal2 = {123:"pera", 234:"sava"}

print lokal
print lokal2

print lokal[234]
print lokal.keys()
print lokal.values()

if 23 in lokal:
    '''if 23 in lokal.keys()'''
    print lokal[23]
else:
    print "nema ga"


if "sava" in lokal:
    print lokal[23]
else:
    print "nema ga"

print lokal.values()
print lokal.keys()

lokal[345] = "Maya"
print lokal

print lokal
print sorted(lokal.keys())

for k in sorted(lokal.keys()):
    print k,lokal[k]

print lokal.keys()
print lokal.values()
zip(lokal.keys(), lokal.values())

for k,v, in zip(lokal.keys(),lokal.values()):
    print k,v

del(lokal[345])

for k,v in lokal.iteritems():
    print k,v