ile=0

for i in list(range(0,101)):
    if i%3 == 0 or i%5 == 0:
        ile +=1
        print(ile)
print(f"ilość podzielnych przez 3 lub 5: {ile}")
