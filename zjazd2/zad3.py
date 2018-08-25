liczby = [1,2,2,2,3,-3,4,5,6,7,-78,8,1,32,-2,2,-3,6,4,5]

ujemn= 0
dodatnie = 0

for i in liczby:
    if i > 0:
        dodatnie += 1
    elif i < 0:
        ujemn += 1

print(f"liczby dodatnie {dodatnie}")
print(f"liczby ujemne {ujemn}")