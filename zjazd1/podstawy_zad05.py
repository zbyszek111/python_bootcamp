print('Wpisz miasto A:')
Miasto_A = input()

print('Wpisz miasto B:')
Miasto_B = input()


print('Wpisz dystans:')
dystans = float(input(f'{Miasto_A} - {Miasto_B}:'))
print('Wpisz cena paliwa:')
cena_paliwo = float(input())

print('Wpisz spalanie:')
spalanie = float(input())
kilometry =100 # lepiej stosowań dzielenie na końcu linijki 
koszt = int(((dystans*spalanie)/kilometry)*cena_paliwo)
koszt1 = ((dystans*spalanie)/kilometry)*cena_paliwo
print(f'Koszt pprzejazdu: {Miasto_A} - {Miasto_B} = {koszt} PLN')
print(f'Koszt pprzejazdu: {Miasto_A} - {Miasto_B} to {koszt1:.2f} PLN')
