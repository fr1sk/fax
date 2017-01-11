import sys

stanje = 'P'
zavrsno = 'P'

prelaz = {('P', '0'): 'N',('P', '1'):'P',('N', '0'):'N',('N','1'):'P'}


while True:
    try:
        c = raw_input("unesi 0 ili 1")
    except EOFError:
      break

    stanje = prelaz[(stanje, c)]
    print stanje

if stanje is zavrsno:
    print "ima paran broj nula"
else:
    print "stanje ima neparan broj nula"