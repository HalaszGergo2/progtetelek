from Szek import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("Piros", 4)
peldany3 = Szek("Barna", 5)
print(peldany1.__str__())
print(peldany2)
print(peldany3)

szekek = [peldany1, peldany2, peldany3]

def labakSzama():
    print("Összesen hány db székláb van a teremben: ", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")


labakSzama()

def maxLabSzine():
    maxIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtönn lábbal rendeklező szék színe: {szekek[maxIndex].szin}")
maxLabSzine()