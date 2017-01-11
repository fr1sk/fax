import re, sys

if len(sys.argv)==1:
    exit("nedovoljno argumenata")

regexMali = re.compile(r"klk(199[0-9]|20(0[0-9]|1[0-6]))\.html", re.I)

if regexMali.match(sys.argv[1]) is None:
    exit("datoteka pogresnog formata")

try:
    with open(sys.argv[1], "r") as f:
        input = f.read()

except IOError:
    exit("greska prilikom ucitavanja datoteke")

#
# <rank>1</rank>
#         <napredak>-1</napredak>
#         <drzava>GBR</drzava>
#         <ime>Andy Murray</ime>
#         <godine>29</godine>
#         <bodovi>13540</bodovi>

regex = re.compile(r'<teniser\s+rb="(?P<broj>[0-9])"\s*>\s*'+
                    r'(?=.*?<rank>\s*(?P<rank>\d)\s*</rank>)'+
                    r'(?=.*?<napredak>\s*(?P<napredak>[+-]?\d+)\s*</napredak>)'+
                    r'(?=.*?<drzava>\s*(?P<drzava>[A-Z]{3})\s*</drzava>)'+
                    r'(?=.*?<ime>\s*(?P<ime>[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s*</ime>)'
                    r'(?=.*?<godine>\s*(?P<god>\d+)\s*</godine>)'+
                    r'(?=.*?<bodovi>\s*(?P<bodovi>\d+)\s*</bodovi>)'+
                   r'.*?'+
                   r'</teniser>', re.I | re.S)

#for m in regex.finditer(input):
    #print m.groups()

#-m da se pomeraju sve o njima
#-c DDD drzava
#-o 20 30 od 20 do 30 god
#bez opcije ceo spisak

katalog = {}
for m in regex.finditer(input):
    katalog[m.group('broj')] = [m.group('ime'),m.group('rank'),m.group('drzava'),m.group('napredak'),m.group('god'),m.group('bodovi')]

#print katalog

m=c=o=False
if len(sys.argv)==2:
    c=o=m=True
elif sys.argv[2]=='-c':
    if re.match(r"[A-Z]{3}",sys.argv[3], re.I) is not None:
        c = True
elif sys.argv[2]=='-m':
    m=True
elif sys.argv[2]=='-o':
    if re.match(r"\d{1,2}",sys.argv[3], re.I) is not None and re.match(r"\d{1,2}",sys.argv[4], re.I) is not None:
        o=True




for k,v in katalog.items():
    if len(sys.argv)==2:
         print v[0:]
    elif m:
        if v[3]!=0:
            print v[0:]
    elif c:
        if v[2]==sys.argv[3]:
            print v[0:]
    elif o:
        if v[4]>sys.argv[3] and v[4]<sys.argv[4]:
            print v[0:]

