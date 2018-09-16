import json


def zapisz(dane):
    with open("pracownicy.json", 'w') as f:
        json.dump(dane, f)


def wypisz(pracownicy):
    for nr, pracownik in enumerate(pracownicy, start=1):
        print(
            f"- [{nr}] {pracownik['imie']} {pracownik['nazwisko']}, "
            f"rok urodzenia: {pracownik['rok_urodzenia']}, "
            f"pensja: {pracownik['pensja']}"
        )


def dane_do_zapisu():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))

    dane = {
        "imie": imie,
        'nazwisko': nazwisko,
        'rok_urodzenia': rok_urodzenia,
        'pensja': pensja
    }

    return dane


try:
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy = []

# Pytamy jakaś akcję użytkownik chce wykonać d-dodaj, w-wypisz
action = input("Co chcesz zrobić? [d-dodaj, w-wypisz]")

if action == 'd':
    dane = dane_do_zapisu()
    pracownicy.append(dane)
    zapisz(pracownicy)

elif action == 'w':
    wypisz(pracownicy)
