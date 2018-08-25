print('podal liczbę A:')
A = int(input('liczba A:'))
print(A%2==0 and A%3==0 \
	and A>10 or A==7)
	# do obcięcia linii kodu stosowany jest \

print((A%2==0) & (A%3==0) \
	& (A>10) | (A==7))