# program pyta ile wynosi iloczyn
from random import randint
zakres = 10
# los całkowite liczby
x= randint(1, zakres)
y= randint(1, zakres)
print(f'podaj iloczyn liczb: {x}*{y}')
proby = 0

while True:
    iloczyn = int(input('podaj wynik:'))
    proby +=1
    if iloczyn==x*y:
        print(f'dobrze,  wynik to {iloczyn}')
        break
    else:
        print('sproboj jeszcze')
print(f'liczba prob {proby}')