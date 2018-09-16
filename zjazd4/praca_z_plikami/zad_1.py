import sys

print(sys.argv)
try:

    wejscie = sys.argv[1]
    with open(sys.argv[1]) as f:
        dane = f.read()
        dane = dane.splitlines()
        for i, linia in enumerate(dane, start=1):
            print(f"{i}: {linia}")

except IndexError:
    print(f.read())