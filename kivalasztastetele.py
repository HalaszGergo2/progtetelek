import math


def kivalasztas2():
    prim = False
    n = 9999
    while(prim):
        n += 1
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    print(n)


kivalasztas2()