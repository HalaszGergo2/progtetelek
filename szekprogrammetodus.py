from Szek import Szek


def peldanyokListaban():
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("Piros", 4)
    peldany3 = Szek("Barna", 5)
    szekek = [peldany1, peldany2, peldany3]
    return szekek


def listakiir(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])


# rövid verzió
# listakiir(peldanyokListaban())


# hosszú verzió:
szeklista = peldanyokListaban()
listakiir(szeklista)


def osszegzes(szekek):
    print("Összesen hány db székláb van a teremben: ", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")


def maxKivalasztas(szekek):
    maxIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtönn lábbal rendeklező szék színe: {szekek[maxIndex].szin}")


def megszamlalas(szekek):
    print("Hány 4-nél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1
    print(db)


def eldontes(szekek):
    print("Van-e piros 4 lábú szék: ", end="")
    van = False
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == "Piros" and szekek[index].labszam == 4:
            van = True
    if van:
        print("Van")
    else:
        print("Nincs")


osszegzes(szeklista)
maxKivalasztas(szeklista)
megszamlalas(szeklista)
eldontes(szeklista)
