tekst = input('podaj napis')
liczniki = {}

for i in tekst.lower():
    if i in liczniki:
        liczniki[i] += 1
    else:
        liczniki[i] = 1

# print(f' litera {i} wyst apiła {liczniki[i]}')

for litera in tekst.lower():
    liczniki[litera] = liczniki.get(litera, 0) + 1
    print(f' litera {litera} wyst apiła {liczniki[litera]}')
