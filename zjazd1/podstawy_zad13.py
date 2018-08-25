ile_dni = 7
i = 1
suma=0
while i <= ile_dni:
    temp=float(input('podaj temperature'))
    i+=1
    suma += temp
print(f'średnia temperatura{suma/ile_dni}')    