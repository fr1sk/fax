pitanja = ["ime", 'zanimanje', "mesto boravka"]
odgovori = ["Marija", "programer", "Beograd"]

for p,o in zip(pitanja, odgovori):
    print "Tvoje %s je? Moje %s je %s.\n" %(p,p,o)

for p,o in zip(pitanja, odgovori):
    print "Tvoje {0} je? Moje {0} je {1}.\n".format(p,o)

for p,o in zip(pitanja, odgovori):
    print "Tvoje %(pit)s je? Moje %(pit)s je %(odg)s.\n" %{"pit":p,"odg":o}
