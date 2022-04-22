scren = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def PrintMatrix(scren):
    for i in range(0, len(scren)):
        for j in range(0, len(scren[i])):
            if scren[i][j] == 1 or scren[i][j] == 2:
                print('██', end=' ')
            else:
                print("{:02d}".format(scren[i][j]), end=' ')
        print()
    print('')

PrintMatrix(scren)

for i in range(0, len(scren) - 1):
    for j in range(0, len(scren[i]) - 1):
        if scren[i + 1][j] == 2:
            scren[i][j] = 1
        if scren[i - 1][j] == 2:
            scren[i][j] = 1
        if scren[i][j + 1] == 2:
            scren[i][j] = 1
        if scren[i][j - 1] == 2:
            scren[i][j] = 1

PrintMatrix(scren)