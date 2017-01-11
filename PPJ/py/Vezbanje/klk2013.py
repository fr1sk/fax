import re,sys

if len(sys.argv)<4:
    exit("nedovoljan broj argumenata")

if re.match(r'.*?\.txt',sys.argv[1], re.I) is None:
    exit("neispravna datoteka")

regexDatum = re.compile(r'.*?'
                        r'(([012][0-9])|(3[01])\.(01|03|05|07|08|10|12))|'+
                        r'(([012][0-9])|(30)\.(04|06|09|11))|'+
                        r'(([012][0-9])\.(02))', re.S)

regexSati = re.compile(r'(([01][0-9])|2[0-3]):([0-5][0-9])', re.S)


try:
    with open(sys.argv[1], "r") as f:
        input = f.read()
except IOError:
    exit("neuspesno citanje datoteke")

print input
regexMain = re.compile(r'.*?(?:(?P<datDan>[0-9]+)\.(?P<datMes>[0-9]{2}))\s(?:(?P<satSat>[0-9]{2}):(?P<satMin>[0-9]{2}))(?:.*?\((?P<dana>\d{1,2})\+(?P<sati>\d{1,2}):(?P<min>\d{1,2})|)')

katalog = {}
for m in regexMain.finditer(input):
    katalog[m.group('datMes')] = [m.group('datDan'), m.group('satSat'), m.group('satMin'), m.group('dana'), m.group('sati'), m.group('min'), 0,0]


unetDatum = sys.argv[2]
unetVreme = sys.argv[3]
vreme = str(unetVreme).split(':')
datum = str(unetDatum).split('.')

unetVremeMinuti = int(vreme[0])*60+int(vreme[1])
mesec = int(datum[0])
dan = int(datum[1])
mesecUmin=0
danUmin=dan*24*60

if mesec==1 or mesec==3 or mesec==5 or mesec==7 or mesec==8 or mesec==10 or mesec==12:
    mesecUmin =  31 * 24 *60*mesec
elif mesec==4 or mesec==6 or mesec==9 or mesec==11:
    mesecUmin = 30 * 24 *60*mesec
elif mesec==2:
    mesecUmin = 29*24*60*mesec

sveUmin = unetVremeMinuti+danUmin+mesecUmin
print sveUmin


for k,v in katalog.items():
    if int(k)==1 or int(k)==3 or int(k)==5 or int(k)==7 or int(k)==8 or int(k)==10 or int(k)==12:
         v[6] =  31 * 24 *60*int(k) + int(v[0])*24*60 + int(v[1])*60 + int(v[2])
    elif int(k)==4 or int(k)==6 or int(k)==9 or int(k)==11:
         v[6] = 30 * 24 *60*int(k)+ int(v[0])*24*60 + int(v[1])*60 + int(v[2])
    elif int(k)==2:
         v[6] = 29*24*60*int(k)+ int(v[0])*24*60 + int(v[1])*60 + int(v[2])

print katalog


for k,v in katalog.items():
    if v[3] is not None:
        sveee=int(v[3])*24*60+int(v[4])*60+int(v[5])
        v[7]=sveee + v[6]


for k,v in katalog.items():
    if int(v[7])==0:
        if int(v[6])<sveUmin:
            print k,v
    else:
        if int(v[7]) > sveUmin and int(v[6])<sveUmin:
            print k,v

