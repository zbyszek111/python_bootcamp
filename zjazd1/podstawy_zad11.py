def pozycja(X,Y):
    if (0< X < 9 and 0 < Y < 9):
        return 'prawy górny róg'
    elif (9< X < 91 and 9< Y < 91):
        return 'centrum'
    elif (91< X < 100 and 91< Y < 100):
        return 'lewy dolny róg'
    elif (0< X < 9 and 9< Y < 91):
        return 'górna krawedz'
    elif (0< X < 9 and 91< Y < 100):
        return 'górny prawy róg'
    elif (9< X < 91 and 0< Y < 9):
        return 'lewa krawedz'
    elif (9< X < 91 and 91< Y < 100):
        return 'prawa krawedz'
    elif (91< X < 100 and 9< Y < 91):
        return 'dolna krawedz'
    elif (X > 100 or Y > 100):
        return 'poza krawędzią'
    elif (X < 0 or Y < 0):
        return 'poza krawędzią'
            
X= int(input('podaj wsp.X:'))
Y= int(input('podaj wsp.Y:'))
obl= pozycja(X,Y)
print(obl)