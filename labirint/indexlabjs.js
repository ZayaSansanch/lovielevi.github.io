const labirint = [
[-1, -1, -1, -1, -1, -1, -1],
[1, 0, 0, -1, 0, 0, -2],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, -1, 0, -1, -1],
[-1, -1, 0, 0, 0, -1, -1],
[-1, -1, -1, -1, -1, -1, -1]
]
var iscomoe = 1
var x = 0
var y = 0

funcshion print_labirint():
	for i in range(len(labirint)):
		for j in range(len(labirint[i])):
			if labirint[i][j] == -1:
				print('██', end=' ')
			else:
				print("{:02d}".format(labirint[i][j]), end=' ')
		print()
	print('')
print_labirint()