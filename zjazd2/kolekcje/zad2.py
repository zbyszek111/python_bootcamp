# podaj 10 liczb

liczby = []

while len(liczby) < 10:

    liczby.append(input('podaj liczbe'))
print(liczby)

print(sum(int(liczby)) / len(liczby))
