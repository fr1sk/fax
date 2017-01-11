import re, sys

if len(sys.argv)==1:
    exit("nema dovoljno argumenata komadne linije");

regex = re.compile(r".*\.stn", re.I)

if re.match(regex, sys.argv[1]) is None:
    exit("zadati fajl nema stn extenziju")

try:
    with open(sys.argv[1], "r") as f:
        datoteka = f.read()

except IOError:
    exit("neuspesno citanje datoteke")

regexMain = re.compile(r"{(?P<tag>.*?),\.NE\+(?P<vr>[a-z]{3,5}):\d[a-z]}", re.S)

for m in regexMain.finditer(datoteka):
    print m.groups(), "\n"

output = regexMain.sub(r"<\g<tag>>\g<vr></\g<tag>>", datoteka)
print output

try:
    with open(sys.argv[1][:-3]+"xml", "w") as d:
        d.write("<xml>+\n")
        d.write(output)
        d.write("</xml>+n")

except IOError:
    exit("neuspesno otvaranje datoteke za pisanje: "+sys.argv[1][:-3]+"xml")