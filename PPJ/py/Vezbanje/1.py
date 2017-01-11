import sys, re

if len(sys.argv) == 1:
    exit("nije zadat argument komandne linije")

regex = re.compile(r".*\.txt", re.I)

if re.match(regex, sys.argv[1]) is None:
    print "datoteka nije dobra"

emailRegex = re.compile(r"[A-Za-z][A-Za-z0-9_\.]{4,}@[A-Za-z]+\.(com|net|rs|me)")

try:
    f = open(sys.argv[1], "r")
except IOError:
    exit("greska prilikom otvaranja datoteke")

lista = f.readlines()
print lista

di = dict()


i = 0
for i in range(len(lista)):
    # temp = lista[i]
    # temp = temp[:-1]
    # lista[i] = temp
    lista[i] = lista[i][:-1]

print lista

for linija in lista:
    if re.match(emailRegex, linija) is not None:
        if linija in di.keys():
            di[linija] += 1
        else:
            di.update({linija:1})


print di