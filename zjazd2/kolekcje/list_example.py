imiona = ["Robert", "Kamil", " Piotrek", "Karolina"]

print(imiona)
print(type(imiona))

print(len(imiona))


print("Robert" in imiona)

for imie in imiona:
    print(imie)

print(imiona[2])
print("Ostatnie imię:", imiona[-1])
print("Ostatnie imię:", imiona[-2])
print("Ostatnie imię:", imiona[1])
print("liczy ile razy wystąpi imie Kamil",imiona.count("Kamil"))

print(imiona)
imiona.append("Rafał")
print(imiona)
print(imiona.pop())
print(imiona)
print(dir(imiona))


imiona.remove('Kamil')
imiona = imiona + ["A", "A", "A"]

print(imiona)