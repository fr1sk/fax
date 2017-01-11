#fibonaci
#0 1 1 2 3 5 8 13

#a b
#0 1
#1 1
#1 2
#2 3

def fibonacci (n=5): #default je 5, kao prazan konstruktor
    a,b = 0,1
    niz = []

    while a<n:
        niz.append(a)
        # a <- b
        # b <- b+
        a,b = b, a+b # a ce biti b, a b ce biti a+b

    return niz

print fibonacci(20)
print fibonacci()
print fibonacci #adresu gde se funkcija nalazi