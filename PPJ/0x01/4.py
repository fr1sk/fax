#funkcije prost

def prost(n):
    if n==2:
        return 1

    if n%2 == 0:
        return 2

    for x in range (3,n//2, 2):
        if n % x == 0:
            return x
            break
    #else se izvrsaa ukoliko se izadje kada proje cela petlja
    else:
        return 1

try:
    x = int(raw_input("unesite br veci od 1:"))
    if x <= 1:
        raise ValueError
except ValueError:
    exit("uneti broj nije veci od 1")

#x = 27
d = prost(x)
if d == 1:
    print("%d je prost broj" %x)
elif d == 2:
    print "broj je paran"
else:
    print ("%d = %d * %d " %(x,d,x/d))