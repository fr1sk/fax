pocetno = "P"
zavrsno = 'P'

#brojNula = 0
stanje = pocetno
prelaz = {('P')}

while True:
    try:
        c = raw_input() #kad se pritisne enter tu je kraj ulaza, sve do entera je c
        if c != '0' and c != '1':
            # print ("unesite 0 ili 1")
            # continue
            raise ValueError
    except EOFError:
        break
    except ValueError:
        print ("unesite 0 ili 1")
        continue

    if stanje == 'P':
        if c=='0':
            stanje = 'N'
        #else:
            #stanje = 'P'
    else:
        if c == '0':
            #brojNula += 1
            stanje =  'P'

#if brojNula % 2 == 0:
if stanje == zavrsno:
    print "automat prihvata rec"
    #print "Uneti tekst ima paran broj 0"
else:
    print "Nije uneta rec sa parnim broje 0"
   # print "Nije unetparan broj 0"



