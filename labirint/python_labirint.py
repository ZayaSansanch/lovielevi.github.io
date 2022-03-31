labirint = [
[-1, -1, -1, -1, -1, -1, -1],
[1, 0, 0, -1, 0, 0, -2],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, 0, 0, -1, -1],
[-1, -1, -1, -1, -1, -1, -1]
]
iscomoe = 1
x = 0
y = 0

def print_labirint():
	for i in range(len(labirint)):
		for j in range(len(labirint[i])):
			if labirint[i][j] == -1:
				print('██', end=' ')
			else:
				print("{:02d}".format(labirint[i][j]), end=' ')
		print()
	print('')
print_labirint()

def len_labirint():
	for i in range(len(labirint)):
		for j in range(len(labirint[i])):
			if labirint[i][j] == -2:
				y = i
				x = j
	return(y, x)

y, x = len_labirint()
print(y, x)
while labirint[y][x] == -2:
	for i in range(len(labirint)):
		for j in range(len(labirint[i])):
			if labirint[i][j] == iscomoe:
				if i > 0 and (labirint[i - 1][j] == 0 or labirint[i - 1][j] == -2):
					labirint[i - 1][j] = iscomoe + 1
				if i < len(labirint) - 1 and (labirint[i + 1][j] == 0 or labirint[i + 1][j] == -2):
					labirint[i + 1][j] = iscomoe + 1
				if j > 0 and (labirint[i][j - 1] == 0 or labirint[i][j - 1] == -2):
					labirint[i][j - 1] = iscomoe + 1
				if j < len(labirint[i]) - 1 and (labirint[i][j + 1] == 0 or labirint[i][j + 1] == -2):
					labirint[i][j + 1] = iscomoe + 1
	iscomoe += 1 
	print_labirint()