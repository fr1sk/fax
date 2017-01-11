import sys, re

if len(sys.argv) == 1:
    exit("nedovoljan broj argumenata komandne linije")
elif re.match(r".*\.html", sys.argv[1]) is None:
    exit("tebra daj html")


with open(sys.argv[1]) as f:
    temp = f.read()

komplikovaniRegex = re.compile(r"<tr>"
                                +r"\s*<td>\s*[A-Z][a-z]+ [A-Z][a-z]+</td>\s*"
                                +r"<td>\s*\d\s*</td>\s*"
                                +r"<td>\s*\d\s*</td>\s*"
                                +r"</tr>", re.M | re.S)

if re.match(komplikovaniRegex, temp) is not None:
    print "ima"

