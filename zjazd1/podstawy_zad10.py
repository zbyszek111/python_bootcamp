def oblicz(operacja, arg1, arg2):
    if dzialanie =='+':
        return liczba1+liczba2
    elif dzialanie =='-':
        return liczba1-liczba2
    elif dzialanie =='/':
        return liczba1/liczba2
    elif dzialanie =='*':
        return liczba1*liczba2
    else:
        raise ValueError(f'Niezxnana operacja')

try:
    liczba1 = int(input('podaj liczbę1:'))
    liczba2 = int(input('podaj liczbę2:'))
    dzialanie = input('wpisz działanie')
    wynik = oblicz(dzialanie, liczba1, liczba2)
    print(f'Wynik:{wynik}')
    
except Exception as e:
    print(f'Nastąpił błąd:{e}')
    
print('Koniec')