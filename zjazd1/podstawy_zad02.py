A=3
B=9
H=6.5
C= 0.5*(A+B)*H
print('pole trapezu wynosi:',C, 'cm^2')
print(C)

# inna opcja 
def trapez(A,B,H):
    return 0.5*(A+B)*H
print(trapez(A,B,H))

# obsługa fstringi
# obecnie najbardziej zalecane podejście
print(f'Pole trapezu wynosi: {C}')


#sposób popularny w pythonie 2 i dostępny
print('Pole trapezu wynosi: %.1f' % C)
print('Pole trapezu wynosi: %d' % C)


#wypisywanie za pomoca fstring
imie1= 'Ala'
imie2= 'Ola'
x=10
print(f'{imie1} ma {x} kotów')
print(f'{imie2:2} ma {x} kotów')
s=f'{imie1} ma {x} kotów'
print(s)


print('Jak masz na imię?')
tekst = input()
print(f'Witaj {tekst}!')

print('Podaj promień koła')
r = float(input())
print(f'zmienna r jest wypu {type(r)}')
PI=3.14
pole = PI*r**2
print(f'Pole kola {pole}')






