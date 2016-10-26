import re, sys, os
#arg /home/fr1sk/Documents/PycharmProjects/PPJ/0x01

homedir = "."

if len(sys.argv) > 1:
    homedir = sys.argv[1]

studenti = {}

try:
    f = open(homedir+"/"+"indeksi", "r")
    for linija in f.readlines():
        if re.match(r"^m[irmnvl]\d{5},\s*[A-Za-z]+( +[A-Za-z]+)+", linija) is not None:
            if linija[-1] == '\n':
                linija = linija[:-1] #linija.pop()
            info = re.split(r",\s*",linija)
           #print info
            studenti[info[0]] = info[1]

    f.close()
except IOError:
    exit("neuspesno citanje " + homedir +"/indeksi")

re_zadatak = re.compile(r"([1-9]\d*)\.(c(?:pp)?|java|pas)$")

resenja = {}
maxBrZadataka = 0

#print studenti
for f in os.listdir(homedir):
    #print f
    stud_dir = os.path.join(homedir,f)
    if os.path.isdir(stud_dir) is True and f is studenti.keys():
        print f, stud_dir
        for sf in os.listdir(stud_dir):
            #print sf
            sf_path = os.path.join(stud_dir,sf)
            m = re_zadatak.match(sf)
            if os.path.isfile(sf_path) and m is not None:
                #print(sf,sf_path)
                zadatak = int(m.group(1))
                resenja[(f,zadatak)] = m.group(2)
                if zadatak > maxBrZadataka:
                    maxBrZadataka = zadatak

print resenja
for alas, ime in studenti.items():
    print alas, ime
    for i in range(1, maxBrZadataka+1):
        #print(alas,i)
        if(alas, i) in resenja:
            print resenja[(alas,i)]
        else:
            print ' - '