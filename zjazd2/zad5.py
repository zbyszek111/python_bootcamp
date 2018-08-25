# program zamieniający miejscami element najwiekszy z najmniejszym


liczby = [5, 2, 1, 4, 3]
min_ = None
max_ = None

# tu zamieniemy indeksy min z max

# na indeksach operacja
print(f"przed: {liczby}")
for i in range(len(liczby)):
    if min_ is None or liczby[i] < liczby[min_]:
        min_ = i
    if max_ is None or liczby[i] > liczby[max_]:
       max_ = i
print(f"indeks min: {min_}")
print(f"indeks max: {max_}")

#temp = liczby[min_]
#liczby[min_]= liczby[max_]
#liczby[max_]= temp
liczby[max_], liczby[min_] = liczby[min_], liczby[max_]

print(f"po: {liczby}")