import re, sys

if len(sys.argv)==1:
    exit("nema dovoljno argumenta komande linije")

try:
    with open("PetiDrugi.xml", "r") as f:
        input = f.read()

except IOError:
    exit("neuspesno otvaranje datoteke")

#-a autor
#-c cena
#-i izdavac
#-g godina

regex = re.compile(r'<knjiga\s+rbr\s*=\s*"(?P<rbr>[1-9]\d*)"\s*>\s*'+
                    r"(?=.*?<naslov>\s*(?P<naslov>.+?)\s*</naslov>\s*)"
                   # r"(?=.*?<naslov>\s*((?P=ime)[A-Z][a-z]+)\s+((?P=prezime[A-Z][a-z]+))\s*</naslov>\s*"
                    r"(?=.*?<autor>\s*(?P<autor>[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s*</autor>\s*)"+
                    r"(?=.*?<izdavac>\s*(?P<izdavac>.*?)\s*</izdavac>\s*)"+
                    r"(?=.*?<godina_izdanja>\s*(?P<godina>[12]\d{3})\s*</godina_izdanja>\s*)"+
                    r'(?=.*?<cena\s+valuta\s*=\s*"(?P<valuta>[a-z]{3})"\s*>\s*(?P<cena>\d+)\s*</cena>\s*)'+
                    r".*?"+
                    r"</knjiga>\s*" , re.S)

autor=cena=izdava=godina=False
naslov = sys.argv[-1]

for i in range(1, len(sys.argv)):
    if sys.argv[i]=='-a':
        autor = True
    if sys.argv[i]=='-c':
        cena = True
    if sys.argv[i]=='-g':
        godina = True
    if sys.argv[i]=='-i':
        izdava = True

if len(sys.argv)==2:
    autor=cena=godina=izdava=True

katalog = {}
for m in regex.finditer(input):
    katalog[m.group('rbr')] = [m.group('naslov'), m.group('autor'), m.group('cena'), m.group('godina'), m.group('izdavac'), m.group('valuta')]


for k,v in katalog.items():
    if v[0] == naslov:
      #  podaci = v[1:] #u novu promenjivu sve od naslova
        if autor:
            print v[1]
        if cena:
            print v[2], v[5]
        if godina:
            print v[3]
        if izdava:
            print v[4]

if not autor or cena or godina or izdava:
    for k,v in katalog.items():
        print v






