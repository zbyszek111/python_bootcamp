i=0

while True:
    i+=1
    txt = input('podaj kolejną liczbę:')
    if txt == 'koniec': 
        break        
    liczba= int(txt)
    if i==1:
        max = min=liczba
    else:
        if liczba > max:
            max=liczba
        if liczba < min:
            min=liczba
        
print(f'Maksimum: {max}')
print(f'Minimum: {min}')