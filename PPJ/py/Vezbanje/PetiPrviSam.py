import re,sys

if len(sys.argv) == 1:
    exit("nedovoljan broj argumenata")

maliRegex = re.compile(r".*?\.stn", re.I)

if re.match(maliRegex, sys.argv[1]) is None:
    exit("losa datoteka")

try:
    with open(sys.argv[1],"r") as f:
        input = f.read()

except IOError:
    exit("neuspesno citanje datoteke")

regex = re.compile(r"{(?P<sadrzaj>.*?),\.NE\+(?P<tag>[a-z]+):\d[a-z]}", re.S)

edit = re.sub(regex, r'<\g<tag>>\g<sadrzaj></\g<tag>>', input)

try:
    with open(sys.argv[1][:-4]+"Sam.xml", "w") as f:
        f.write("<xml>\n")
        f.write(edit)
        f.write("\n</xml>")

except IOError:
    exit("neuspesno otvaranje datoteke")

