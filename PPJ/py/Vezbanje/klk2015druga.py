import re, sys

def racunajTempo(x):
    vreme = str(x).split(':')
    sati = float(vreme[0])*60
    minuti = float(vreme[1])
    sekunde = float(vreme[2])/60
    tempo = float(sati+minuti+sekunde)
    return tempo

if len(sys.argv)==1:
    exit("nedovoljan broj argumenata")

if re.match(r'.*?.html', sys.argv[1], re.I) is None:
    exit("neispravna datoteka")

try:
    with open(sys.argv[1], "r") as f:
        input = f.read()

except IOError:
    exit("neuspesno otvaranje datoteke")

#rang, sratrni broj, prezime i ime, godina, zemlja, vreme za 5, 10, 15,20km, vreme za celu trku
#<TR class=r0><td>1</td><td>3001</td><td>PUHAR ROK</td><td>1992</td><td>SLO</td><td>0:15:09</td><td>0:31:05</td><td>0:47:27</td><td>1:04:01</td><td>1:07:40</td><TD></TD></TR>
regex = re.compile(r'<TR\sclass=r0>'
                    r'\s*<td>\s*(?P<rang>\d+)\s*</td>\s*'
                    r'\s*<td>\s*(?P<startBr>\d+)\s*</td>\s*'
                    r'\s*<td>\s*(?P<ime>\w+\s\w+)\s*</td>\s*'
                    r'\s*<td>\s*(?P<godine>\d+)\s*</td>\s*'
                    r'\s*<td>\s*(?P<zemlja>[A-Z]{3})\s*</td>\s*'
                    r'\s*<td>\s*(?P<km5>\d{1,2}:\d{1,2}:\d{1,2})\s*</td>\s*'
                    r'\s*<td>\s*(?P<km10>\d{1,2}:\d{1,2}:\d{1,2})\s*</td>\s*'
                    r'\s*<td>\s*(?P<km15>\d{1,2}:\d{1,2}:\d{1,2})\s*</td>\s*'
                    r'\s*<td>\s*(?P<km20>\d{1,2}:\d{1,2}:\d{1,2})\s*</td>\s*'
                    r'\s*<td>\s*(?P<celaTrka>\d{1,2}:\d{1,2}:\d{1,2})\s*</td>\s*'
                   r'.*?'
                   r'<TD></TD>'
                   r'</TR>', re.S|re.I)

#-p tempo; -c DDD drzava;
katalog = {}
for m in regex.finditer(input):
    #print m.groups()
    katalog[m.group('startBr')] = [m.group('ime'), m.group('godine'), m.group('zemlja'), m.group('rang'), m.group('km5'), m.group('km10'), m.group('km15'), m.group('km20'), m.group('celaTrka'), float(0), float(0), float(0), float(0),float(0)]


c=o=p=False
for k,v in katalog.items():
    v[9] = round(racunajTempo(v[4]) / 5,3)
    v[10] = round(racunajTempo(v[5]) / 10, 3)
    v[11] = round(racunajTempo(v[6]) / 15, 3)
    v[12] = round(racunajTempo(v[7]) / 20, )
    v[13] = round(racunajTempo(v[8]) / 21, 3)

#print katalog


if len(sys.argv)>=3:
    if sys.argv[2]=='-c':
        c = True
    if sys.argv[2]=='-o':
        o = True
    if sys.argv[2]=='-p':
        p = True


for k,v in katalog.items():
    if c:
        if v[2]==sys.argv[3]:
            print k,v
    if o:
        godine = 2015 - int(v[1])
        if godine>int(sys.argv[3]) and godine<int(sys.argv[4]):
            print k,v
    if p:
        if v[13]<float(sys.argv[3]):
            print k,v


if c is False and o is False and p is False:
    print katalog
#
# (?<tr\sclass=r0>)<td>[0-9]+</td><td>[0-9]+</td><td>[a-z]+ [a-z]+</td><td>
# (198[6-9]|199[0-2])</td><td>(SRB|SLO)</td><td>([0-9]+:[0-9]+:[0-9]+)
# </td><td>([0-9]+:[0-9]+:[0-9]+)</td><td>([0-9]+:[0-9]+:[0-9]+)</td><td>
# ([0-1]+:[0-9]+:[0-9]+)</td><td>([0-9]+:[0-9]+:[0-9]+)</td><td></td></tr>'

# regex = re.compile("<tr>\s*"
#                    '\s*<td\sclass="rank-cell">\s*(?P<rank>\d+)\s*</td>\s*'
#                      '\s*<td\sclass="move-cell">\s*(?P<move>\+?-?\d+)\s*</td>\s*'
#                     '\s*<td\sclass="country-cell">.*?alt="(?P<country>[A-Z]{3})".*?</td>\s*'
#                     '\s*<td\sclass="player-cell">\s*(?P<player>[A-Z][a-z]+\s[A-Z][a-z]+)\s*</td>\s*'
#                     '\s*<td\sclass="age-cell">\s*(?P<age>\d+)\s*</td>\s*'
#                     '\s*<td\sclass="points-cell">\s*(?P<points>\d+)\s*</td>\s*'
#                     '\s*<td\sclass="tourn-cell">\s*(?P<tourn>\d+)\s*</td>\s*'
#                     '\s*<td\sclass="pts-cell">\s*(?P<pts>\d+)\s*</td>\s*'
#                     '\s*<td\sclass="next-cell">\s*(?P<next>\d+)\s*</td>\s*'
#                     ".*?"
#                    "</tr>", re.S)

