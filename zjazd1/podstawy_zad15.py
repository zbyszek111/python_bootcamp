from random import randint, randrange

zakres=9
# wsp skarbu
i= randint(0,zakres)
j= randint(0,zakres)
# wsp wstepne gracza
x=randint(0,zakres)
y=randint(0,zakres)

ile_ruch=0
poczatkowa= abs(i-x)+abs(j-y)
odl=poczatkowa
while True:
    
    print(f'pozycja gracza:{x,y}')
    znak=input('podaj kierunek ruchy [wsad]')
    if znak=='a':
        x-=1
    elif znak=='d':
        x+=1
    elif znak=='w':
        y+=1
    elif znak=='s':
        y-=1
    ile_ruch+=1
    if x < 0 or y<0 or x>zakres or y>zakres:
        print('game over')
        break
    if ile_ruch>poczatkowa:
        i= randint(0,zakres)
        j= randint(0,zakres)
        ile_ruch=0
        poczatkowa= abs(i-x)+abs(j-y)
    if (x,y)==(i,j):
        print('znalazles skarb')
        break
    
    nowaodl= abs(i-x)+abs(j-y)
    if randrange(5)>0:
        if nowaodl < odl:
            print('ciueplo')
        else:
            print('zimno')
    odl=poczatkowa
    
        
   
    
    
    
    