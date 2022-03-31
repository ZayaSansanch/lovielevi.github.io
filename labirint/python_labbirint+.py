def parse_labirint(lab):
	res = []
	lines = lab.split('\n')
	for i in range(len(lines)):
		if lines[i] == "":
			continue
		res_line = []
		for j in range(len(lines[i])):
			if lines[i][j] == "█":
				res_line.append(-1)
			elif lines[i][j] == "o":
				res_line.append(1)
			elif lines[i][j] == "x":
				res_line.append(-2)
			else:
				res_line.append(0)
		res.append(res_line)
	return res

def find_end(lab):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == -2:
				return (i, j)
	return (0, 0)


def print_labirint(lab):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == -1:
				print('███', end=' ')
			else:
				print("{:03d}".format(lab[i][j]), end=' ')
		print()
	print('')

labirint = parse_labirint("""
██████████████████████████
█o        █    █ ██ ██ █x█
██ ███ █ ███ █ █  █      █
█   █  █  █  █ ██ █ █ ████
█ █ ██ ██ █ ██ █  █ ███ ██
█████  ██   ██   ██      █
█     ██████████████████ █
█ ██ ██    █   █         █
█ █████ ██ █ █ █ █████████
█       █    █           █
██████████████████████████
""")
end_x, end_y = find_end(labirint)

iscomoe = 1

print_labirint(labirint)

while labirint[end_x][end_y] == -2:
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
	print_labirint(labirint)