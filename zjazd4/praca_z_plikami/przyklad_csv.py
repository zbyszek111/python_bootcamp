import csv

with open("pliki_wejsciowe/ludziki.csv") as f:
    dane =csv.reader(f)
    for row in dane:
        print(row)