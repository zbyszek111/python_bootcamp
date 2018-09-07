produkty = {
    'ziemniaki': 1.99,
    'bataty': 6.99,
    'pomidory': 2.5,
    'piwo': 7
}

magazyn = {
    'ziemniaki': 10,
    'bataty': 10,
    'pomidory': 10,
    'piwo': 10
}
koszyk = {}


for p in produkty:
    print(f"- {p} - {produkty[p]} PLN ")


while True:

    komenda = input("Co chcesz zrobić: DODAJ / KUP: ")

    if komenda == "KUP":
        # ścieżka zakupów
        jaki_produkt = input("Jaki produkt chcesz kupić (wpisz k by zakończyć)? ")
        if jaki_produkt == 'k':
            break
        ile = float(input(f"Ile chcesz kupić: {jaki_produkt}? "))
        if magazyn[jaki_produkt] >= ile:
            koszyk[jaki_produkt] = ile*produkty[jaki_produkt]
            magazyn[jaki_produkt] -= ile
        else:
            print("Sorrry nie mamy tyle produktu")
    elif komenda == "DODAJ":
        # ścieżka dodania do magazynu
        # ...
        pass
    else:
        print("Nieprawidłowa komenda ")

koszt_calkowity = 0
for wklad in koszyk:
    koszt_calkowity += koszyk[wklad]
    print(f" - Koszt - {wklad} - {koszyk[wklad]}")

print(f"SUMA: {koszt_calkowity}")