def czy_palindrom(n):
    if n == n[::-1]:
        print(f'{n}, {n[::-1]}')
        print(True)
    else:
        print(f'{n}, {n[::-1]}')
        print(False)


czy_palindrom('kajak')

czy_palindrom('python')