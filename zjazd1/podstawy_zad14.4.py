max = min = None
while True:
    txt = input('podaj kolejną liczbę:')
    if txt == 'koniec': 
        break
    # teraz wyłapujemy i ignorujemy wpisany tekst
    try:
        liczba= int(txt)
        if max is None or liczba > max:
            max=liczba
        if min is None or liczba < min:
            min=liczba
    except Exception:
        pass
        
print(f'Maksimum: {max}')
print(f'Minimum: {min}')
