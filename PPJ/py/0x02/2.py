import re, sys

# todo argumenti i opcije
if len(sys.argv) == 1:
    exit('Program se poziva sa : python %s (-[aicg]) naslov')

if len(sys.argv) == 2:
    naslov = sys.argv[1]

autor=cena=godina=izdavac=False;

if sys.argv[1][0] == '-':
    if sys.argv[1][1] == 'a':
        autor = True
    elif sys.argv[1][1] == 'c':
        cena = True
    elif sys.argv[1][1] == 'g':
        godina = True
    elif sys.argv[1][1] == 'i':
        izdavac = True
    else:
        exit("poziv sadrzi nepoznatu opciju")

    '''
    if re.match(r'-[aicg]+', sys.argv[1]):
        if 'a' in sys.argv[1]
            autor = True
        ... i tako za svaki (izdava, godina, cena...)
    '''
    naslov = sys.argv[2]
else:
    naslov = sys.argv[1]

try:
    with open("2.xml", "r") as f:
        sadrzaj = f.read()
except IOError:
    exit("Neuspesno otvaranje datoteke 2.xml")

#print sadrzaj


reKnjiga = re.compile(r'<knjiga\s+rbr\s*=\s*"(?P<rbr>[1-9]\d*)"\s*>\s*'
                      + r"(?=.*?<naslov>\s*(?P<naslov>.*?)\s*</naslov>)"
                       + r"(?=.*?<autor>\s*(?P<autor>[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s*</autor>)"
                       + r"(?=.*?<izdavac>\s*(?P<izdavac>.*?)\s*</izdavac>)"
                       + r"(?=.*?<godina_izdanja>\s*(?P<godina>[12]\d{3})\s*</godina_izdanja>)"
                      + r'(?=.*?<cena\s+valuta\s*=\s*"(?P<valuta>[a-z]{3})">\s*(?P<cena>0|[1-9]\d*)\s*</cena>)'

                      + r".*?"
                      + r"</knjiga>", re.S)

# ?: taj ceo deo je za proveru ali se ne racuna za group i groups
katalog = {}
for m in reKnjiga.finditer(sadrzaj):
    # katalog[m.group('rbr')] = [m.group('naslov'), m.group('autor'), m.group('izdavac'), m.group('godina'),
    #                            m.group('cena'), m.group('valuta')]
    #print m.group(),

    print m.groups()
exit()
podaci=[]
for k,v in katalog.items():
    #print k,v
    if v[0] == naslov:
        podaci = v[1:]#[autor, izdavac, godina, cena, valuta]

if autor:
    print podaci[0]
elif izdavac:
    print podaci[1]
elif godina:
    print podaci[2]
elif cena:
    print podaci[3]+podaci[4]
else:
    for info in podaci:
        print info
