max = float('-Inf')
min = float('Inf')
while True:
    txt = input('podaj kolejną liczbę:')
    if txt == 'koniec': 
        break        
    liczba= float(txt)
    if liczba > max:
        max=liczba
    if liczba < min:
        min=liczba
print(f'Maksimum: {max}')
print(f'Minimum: {min}')