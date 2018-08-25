x = 'Ala ma kota'
#for i in x:
 #   print(i)

print(x.title())


# print(dir(x))

napis = input('wpisz coś: ')

ile_samoglosek = 0
SAMOGLOSKI = "aeiouy"


for i in napis:
    if i.lower() in SAMOGLOSKI:
        ile_samoglosek +=1
print(f' znalezioni : {ile_samoglosek} samogłosek')
