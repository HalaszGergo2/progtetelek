import math


def kivalasztas(szam):
    lista = []
    for i in range(2, int(math.sqrt(szam)+1)):
        if szam % i == 0:
            lista.append(i)
    return lista

print(kivalasztas(10007))

def kivalasztas(szam):
    lista = []
    oszto = 2
    while oszto <= math.sqrt(szam):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista