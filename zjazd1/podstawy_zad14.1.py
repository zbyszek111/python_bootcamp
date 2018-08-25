licznik = 0
suma = 0
while True:
    liczba = input('podaj kolejną liczbę:')
    if liczba == 'koniec': 
        break
    suma+=int(liczba)
    licznik+=1
        
print(f'suma liczb {suma}')
if licznik > 0:
    print(f'średnia liczb to: {suma/licznik}')