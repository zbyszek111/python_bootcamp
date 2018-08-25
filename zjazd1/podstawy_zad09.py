from datetime import datetime

rok = datetime.today().year

print('podaj rok urodzenia')
liczba = int(input())
wiek = rok - liczba


if wiek >= 18:
    print('Pełnoletni!')
else:	
	print('Niepełnoletni!')