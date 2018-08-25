tekst = "Ala ma <kota>, kot ma Ale"
start = tekst.find("<")
stop = tekst.find(">")
print(len(tekst[start+1: stop]))
print(stop-start-1)


czy_miedzy = False
licz_miedzy = 0

for l in tekst:
    if l == "<":
        czy_miedzy = True
    elif l == ">":
        czy_miedzy = False
    elif czy_miedzy:
        licz_miedzy += 1
print(f'licz znakow pomiedzy "<>": {licz_miedzy}')
