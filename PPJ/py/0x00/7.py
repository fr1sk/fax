import re,sys

if len(sys.argv) == 1:
    exit("neophodno je zadati txt datoteku kao argument")

if re.match(r".*\.txt$",sys.argv[1]) is None:
    exit("Treba mi .txt datoteka")

try:
    f = open(sys.argv[1], "r")
except IOError:
    exit("Neuspesno otvaranje datoteke")

print f.readlines() #vraca listu linija u datoteci
print f.read() #cita datteku

#for linije in f.readlines():
