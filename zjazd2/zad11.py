li =input('podaj liczby')
zbior = set()
l_p =set()

for i in li:
    zbior.add(i)
print(zbior)

for l in range(0,101):
    if l%2==0:
        l_p.add(l)
print(l_p)

# rozwoazanie 2

liczby = set()

while True:
    komenta = input('podaj liczbe lub k')
    if komenta == 'k':
        break
    else:
        liczba = int(komenta)
        liczby.add(liczba)
print(f' wprowadzono {len(liczby)} unikalnych liczb')

liczby_parzyste = set(range(0,101,2))
print(f' w tym parzystych od 0 do 10 jest {len(liczby & liczby_parzyste)}')

