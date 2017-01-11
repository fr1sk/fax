import re, sys

if len(sys.argv)==1:
	exit("dodaj datoteku")
if re.match(r'.*?\.txt$', sys.argv[1], re.S) is None:
	exit('Datoteka treba da se zavrsava sa .txt')
if len(sys.argv)!=4:
	exit('unesi datoteku i njene argumente')
#1.1.
#12.31.
datum = re.match(r'(((1|3|5|7|8|(10)|(12))\.(([012][0-9])|(3[01])))|((4|6|9|(11))\.(([012][0-9])|(30)))|(2\.(([012][0-9]))))', sys.argv[2], re.S)
if datum is None:
	exit('ne valja')
#00:00
#23:59
vreme = re.match(r'(([01][0-9])|(2[0-3])):[0-5][0-9]', sys.argv[3], re.S)
if vreme is None:
	exit('ne valja')

try:
	with open(sys.argv[1], 'r') as f:
		tekst = f.read()
except IOError:
	exit("nista ne valja")
#marko    tty8         :1               11.13 15:19    gone - no logout
#reboot   system boot  4.4.0-34-generic 2.13 13:54   still running
#marko    tty7         :0               12.12 16:48 - crash (1+21:05)

m = re.compile(r'.*?([0-9]+\.[0-9]{1,2})\s([0-9]{2}:[0-9]{2})(?:.*?\((?P<dana>\d{1,2})\+(?P<sati>\d{1,2}):(?P<min>\d{1,2})|)')
katalog = {}
print tekst
for i in m.finditer(tekst):
	print i.groups()
	#print i.group(1), i.group(2), i.group(3), i.group(4), i.group(5)
#	katalog[i.group(1)]=[i.group(2), i.group(3), i.group(4), i.group(5)]