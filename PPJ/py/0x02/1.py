#python skripta koja pretvara stn -> xml

import re, sys

if len(sys.argv) == 1:
    exit ("program se poziva sa: %s datoteka.stn" %sys.argv[0])

if re.match(r'.*\.stn$', sys.argv[1]) is None:
    exit(sys.argv[1] + 'nije .stn datoteka')

try:
    f = open(sys.argv[1], "r")
    sadrzaj = f.read()
    f.close()

    #ili ovako ako samo par linija koristimo
    '''
    with open(sys.argv[1], "r") as f:
        sadrzaj = f.read()
    '''
except IOError:
    exit("neuspesno otvaranje i cintanje datoteke %s" %sys.argv[1])

'''
{ponedeljka, 26.novembra,.NE+date:2s}
'''

#print sadrzaj
regex = re.compile(r"{(.*?),\.NE\+([a-z]+):\d[a-z]}", re.S)

for m in regex.finditer(sadrzaj):
    print m.group(), '\n'


#tekst koj se poklopi sa regexom bice zamenjen sa:
#2 uzima tekst iz druge zagrade a  iz prve zagrade
sadrzaj = regex.sub(r'<\2>\1</\2>', sadrzaj)
print sadrzaj

try:
    #with open(re.sub(r"\.stn$", ".xml", sys.argv[1]), "w") as f:
    with open(sys.argv[1][:-3]+"xml", "w") as f:
        f.write("<xml>\n")
        f.write(sadrzaj)
        f.write("\n</xml>")

except IOError:
    exit("neuspesno otvaranje datoteke za pisanje " +sys.argv[1][:-3]+"xml")