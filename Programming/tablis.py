cila = 0
val = 0
cedimoi = False

print('подсчет волн')

while True:
	for val in range(1, 8):
		cila = input()
		if val == 7:
			print('Седьмой!')
		print(val, cila)

''''''

cila = 0
val = 0
cedimoi = False

print('Подсчет волн')

while True:
	for val in range(1, 8):
		cila = input('Волна:', val, 'Введите силу волны')
		if val == 7:
			print('Седьмой!')
		print(val, cila)