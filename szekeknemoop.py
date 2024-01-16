def szekInit(szin: str, labszam: int):
    print(f"szin: {szin}, lábszám: {labszam}")


szekInit("Kék", 3)
szekInit("Piros", 4)
szekInit("zöld", 5)


def szekStr(szin: str, labszam: int):
    return f"szin: {szin}, lábszám: {labszam}"


print(szekStr("kék", 3))
print(szekStr("piros", 4))
print(szekStr("Zöld", 5))
