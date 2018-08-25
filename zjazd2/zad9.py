produkty = {"buraki":3, "kapusta":1, "marchew":2, "fasola":4}
magazyn = {"buraki":300, "kapusta":100, "marchew":200, "fasola":400}
print(produkty)

koszyk = {}
for p in produkty:
    print(f"- {p} - {produkty} pln")


while True:
    komenda = input("KUP/DODAJ")

    #sciezka zakupow

    if komenda == "KUP":
        jaki_produkt = input("podaj produkt: ")
        if jaki_produkt == 'k':
            print(koszyk)
            break
        ile = float(input(f"ile chcesz kupic  {jaki_produkt} :"))
        if magazyn[jaki_produkt]>= ile:
            koszyk[jaki_produkt]= ile*produkty[jaki_produkt]
            magazyn[jaki_produkt]-= ile
        else:
            print('sorry')
        # sciezka dodanie do magazyny
    elif komenda == "DODAJ":
        # sciezka dodawania do magazynu

    else:
        priunt("niewlasciaw sciezka")


    koszyk[jaki_produkt]= ile*produkty[jaki_produkt]

for wklad in koszyk:
    print(f" Koszt:  - {wklad} - {koszyk[wklad]}")
