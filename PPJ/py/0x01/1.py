import re, sys

if len(sys.argv) == 1 or re.match(r'.*\.txt', sys.argv[1]) is None:
        exit("Neophodan txt kao argument komandne linije");

try:
    f = open(sys.argv[1], "r")

except IOError:
    exit("Neuspesno otvaranje datoteke "+sys.argv[1])

# for linija in f:
#     #re.I - ignore case
#     if re.search(r"(\b[a-zA-z]+\b) +\1+", linija, re.I) is not None:
#         #print linija
#         print re.sub(r"(\b[a-zA-z]+\b) +\1", r"\1+", linija, flags=re.I) #re.sub ako ima linija

#vec iskompajliran regex
ri = re.compile(r"(\b[a-zA-z]+\b)+ \1",  re.I | re.S | re.M)

for linija in f:
    #re.I - ignore case
    if ri.search(linija) is not None:
        print ri.sub(r"\1+", linija)

f.close()