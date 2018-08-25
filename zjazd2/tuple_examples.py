imiona = ("Robert", "Kamil", " Piotrek", "Karolina")

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
print(imiona.count("Kamil"))
