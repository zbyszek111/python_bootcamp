plik = open("pliki_wejsciowe/dane.txt")
print(plik)
plik.close()


with open("pliki_wejsciowe/dane.txt", encoding='utf-8',  mode='r') as plik: # takiej formy wykorzyst aby nie robic close
    print(plik)
    print(plik.readlines()) # trybt r - odczyt w- zaqpis , a- dodaj


print(plik)

