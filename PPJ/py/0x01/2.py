import re,sys

if len(sys.argv) == 1:
    exit("nedovoljan broj argumenata")

if re.match(r".*\.html", sys.argv[1], re.I) is None:
    exit("neispravna datoteka (potreban html)")

try:
    with open(sys.argv[1], "r") as f:
        sadrzaj = f.read()

except:
    exit("neuspesno otvranje i citanje datoteke")

regex = re.compile(r"<tr>\s*"
                   +r"<td>\s*(?P<ime>[A-Za-z]+(?:\s+[A-Za-z]+)+)\s*</td>\s*"
                   +r"<td>\s*(?P<pismeni>0|[1-9]\d?|100)\s*</td>\s*"
                   +r"<td>\s*(?P<usmeni>0|[1-9]\d?|100)\s*</td>\s*"
                   +r"</tr>"
                   )

studenti = []
rezultati = []

for m in regex.finditer(sadrzaj): #regex koj prolazi kroz sadrzaj
    # print m.group()
    # print m.groups() #lista teksta koja uparuje podsablon (regex ogradjen malim zagradama)
    print m.group('ime', 'usmeni', 'pismeni')
    studenti.append(m.group('ime'))
    rezultati.append(float(m.group('pismeni')) + float(m.group('usmeni')))

#sortiranSpisak.append((poeni,ime))
#ovako oako necemo da koristimo dve liste pa kasnije da zipujemo u konacnu jendnu

print studenti
print rezultati

sortiranSpisak = zip(rezultati, studenti)
#print sortiranSpisak, "\n\n"
sortiranSpisak.sort()
#print sortiranSpisak, "\n\n"
sortiranSpisak.reverse()
#print sortiranSpisak, "\n\n"

# i=1
# for i, (poeni, ime) in enumerate(sortiranSpisak):
#     print str(i+1)+ ". "+ime+"\t\t\t"+ poeni


i=0
for poeni,ime in sortiranSpisak:
    print str(i+1) + ". " + ime + "\t\t\t" + str(poeni)
    i += 1

try:
    with open("rezultati.txt", "w") as f:
        i=0
        for poeni,ime in sortiranSpisak:
            f.write( str(i+1) + ". " + ime + "\t\t\t" + str(poeni)+ "\n")
            i += 1

except IOError:
    exit("Neuspesno otvaranje i pisanje u datoteku rezultati.txt")

