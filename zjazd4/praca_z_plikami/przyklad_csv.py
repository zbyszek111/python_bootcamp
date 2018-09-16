import csv
a = []
b = []
with open("pliki_wejsciowe/sales.csv") as f:
    dane =csv.DictReader(f)

    for row in dane:
        a.append((float(row['Revenue'])))
        b.append((float(row['Quantity'])))

aver = sum(a)/len(a)
averb = sum(b)/len(b)
print(f"Average Revenue:{aver}")
print(f"Average Quantity:{averb}")
