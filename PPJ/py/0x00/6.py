import re

poruka = "Odakle dolazi dobro je danas dosao."
uparivac = re.match(r'O[a-z]+',poruka)  #match zahteva da poklapanje pocinje od pocetka niske

if uparivac is not None:
    print uparivac.group()
    print poruka[uparivac.start():uparivac.end()]
    print "Duzina " + str(uparivac.end()-uparivac.start())
    print len(uparivac.group())
else:
    print "Nema ovog poklapanja mikicu bre"

#print uparivac

reci = re.findall(r'\w+',poruka)
reci1 = re.findall(r'\b([a-z])(\w+)\b',poruka)
print reci, "\n"*3
print reci1

uparivac = re.search(r'\b[a-z](\w+)\b',poruka)

if uparivac is not None:
    #print uparivac.group()
    print uparivac.group(0,1,2)
    print uparivac.groups()
    #print uparivac.start()

izmenjena = re.sub(r'\bd(\w+)',r"|\1", poruka)
print izmenjena