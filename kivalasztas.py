def kivalaszt():
    VEGE = 0
    db = 0
    min = 2147483648
    while (szam := int(input("N="))) != VEGE:
        if szam < min:
            min = szam
        db += 1
    print(db, "számból a legnagyobb: ", min)
kivalaszt()
