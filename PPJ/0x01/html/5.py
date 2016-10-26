import re,sys,os
def obradiDatoteku (ime_dat):
    if ime_dat in obradjenih:
        return

    obradjenih.append(ime_dat)

    for f in os.listdir("."):
        print f

    try:
        with open(ime_dat,"r") as f:
        #with open(ime_dat,"r") as f:
            sadrzaj = f.read()
    except IOError:
        exit("Neuspesno otvaranje i citanje "+ime_dat)

    re_link = re.compile(r'<a\s+href\s*=s*"([^"]+)"\s*>.*?</a>', re.I | re.S)

    print "\n", ime_dat
    for m in re_link.finditer(sadrzaj):
        #print m.group(1), m.group()
        if m.group(1) in popularnost:
            popularnost[m.group(1)] += 1
        else:
            popularnost[m.group(1)] = 1
        obradiDatoteku(m.group(1))

    print "\nKRAJ", ime_dat, "\n"

if len(sys.argv) == 1:
   pocetna = "index.html"
elif re.match(r".*\.html$", sys.argv[1]) is not None:
    pocetna = sys.argv[1]
else:
    exit("%s nije HTML datoteka" %sys.argv[1])

popularnost = {}
obradjenih = []
obradiDatoteku(pocetna)


for ime, pop in popularnost.items():
    print ime,pop
