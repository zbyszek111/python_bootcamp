#my_dict = dict()

my_dict = {
    'javascript': "language",
    'ruby': "next language"
}

my_dict["python"] = " The best program ever"
print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(list(my_dict.values()))
lista = list(my_dict.values())

for lan in lista:
    print(my_dict.get(lan, "nie mam tego jeszcze"))

print("python" in my_dict)

print(my_dict.get("c++", "jeszcze nie ma"))