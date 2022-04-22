import random
from PIL import Image

labirint = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -3]
]

for i in range(len(labirint)):
    for j in range(len(labirint[i])):
        img = Image.new('RGB', [i, j], 255)
        data = img.load()

solve = False

def dat(x, y, kl):
    # if kl == "green":
    #     col = [0, 255, 0]
    # if kl == "red":
    #     col = [255, 0, 0]
    # if kl == "blue":
    #     col = [0, 0, 255]
    # if kl == "black":
    #     col = [0, 0, 0]
    # if kl == "wile":
    #     col = [255, 255, 255]
    # else:
    #     col = [255, 255, 255]
    
    data[x, y] = kl

while not solve:
    def print_labirint(aaa):
        for i in range(len(aaa)):
            for j in range(len(aaa[i])):
                if aaa[i][j] == -1:
                    print('██', end=' ')
                # elif aaa[i][j] == 0:
                # 	print('  ', end=' ')
                # elif aaa[i][j] == 1:
                # 	print('ст', end=' ')
                # 	print('фн', end=' ')
                else:
                    print("{:02d}".format(aaa[i][j]), end=' ')
            print()
        print('')
                # elif aaa[i][j] == -3:

    randomoe_chislo = 0 

    for i in range(len(labirint)):
        for j in range(len(labirint[i])):
            if labirint:
                ran = random.random()
                for_ran = random.random()

                if labirint[i][j] == 1:
                    res = 1
                elif labirint[i][j] == -3:
                    res = -3
                else:
                    if ran >= for_ran:
                        res = -1
                    else: 
                        res = 0
                
                labirint[i][j] = res
                # print_labirint(labirint)
    colvo = 0
    # for i in range(len(labirint)):
    # 	for j in range(len(labirint[i])):
    # 		if labirint[i + 1][j] == '██':
    # 			colvo += 1
    # 		if labirint[i - 1][j] == '██':
    # 			colvo += 1
    # 		if labirint[i][j + 1] == '██':
    # 			colvo += 1
    # 		if labirint[i][j - 1] == '██':
    # 			colvo += 1

    # 		if labirint[i][j] == 0:
    # 			ran = random.random()
    # 			for_ran = random.random()
    # 		if ran >= for_ran:
    # 			labirint[i][j] = '██'

    print_labirint(labirint)
    labirint2 = labirint

    """
    -------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    # print('')
    print('Проверяем лабиринт)')
    # print('')

    iscomoe = 1
    x = 0
    y = 0

    def len_labirint():
        for i in range(len(labirint)):
            for j in range(len(labirint[i])):
                if labirint[i][j] == -3:
                    y = i
                    x = j
                if labirint[i][j] == 1:
                    yy = i - 1
                    xx = j - 1
        return(y, x, yy, xx)

    y, x, yy, xx = len_labirint()
    print(y, x)
    solve = True
    while labirint[y][x] == -3:
        found = False
        for i in range(len(labirint)):
            for j in range(len(labirint[i])):
                if labirint[i][j] == iscomoe:
                    if i > 0 and (labirint[i - 1][j] == 0 or labirint[i - 1][j] == -3):
                        labirint[i - 1][j] = iscomoe + 1
                        found = True
                    if i < len(labirint) - 1 and (labirint[i + 1][j] == 0 or labirint[i + 1][j] == -3):
                        labirint[i + 1][j] = iscomoe + 1
                        found = True
                    if j > 0 and (labirint[i][j - 1] == 0 or labirint[i][j - 1] == -3):
                        labirint[i][j - 1] = iscomoe + 1
                        found = True
                    if j < len(labirint[i]) - 1 and (labirint[i][j + 1] == 0 or labirint[i][j + 1] == -3):
                        labirint[i][j + 1] = iscomoe + 1
                        found = True
                    
                    for x in range(img.size[0]):
                        for y in range(img.size[1]):
                            data[x][y] = (0, 0, 0)
                    # if labirint[i][j] > 0:
                    #     dat(j, i, (0, 0, 0))
                    # # else:
                    # #     dat(j, i, (255, 255, 255))

        iscomoe += 1 
        if not found:
            solve = False
            break
    print_labirint(labirint2)
    # if solve:
    #     robot = [[y], [x], [yy], [xx]]
    #     while labirint2[yy][xx] == 1:
    #         for i in range(len(labirint), 0, -1):
    #             for ii in range(len(labirint2), 0, -1):
    #                 for j in range(len(labirint), 0, -1):
    #                     for jj in range(len(labirint2), 0, -1):
    #                         print(ii, jj)
    #                         if labirint2[ii][jj] == -3:
    #                             labirint2[ii][jj] = 'ПП'
    #                         print_labirint(labirint2)
    #                         if i > 0 and (labirint[i - 1][j] == iscomoe - 1 or labirint[i - 1][j] == 1):
    #                             labirint2[i - 1][j] = 'ПП'
    #                         if i < len(labirint) - 1 and (labirint[i + 1][j] == iscomoe - 1 or labirint[i + 1][j] == 1):
    #                             labirint2[i + 1][j] = 'ПП'
    #                         if j > 0 and (labirint[i][j - 1] == iscomoe - 1 or labirint[i][j - 1] == 1):
    #                             labirint2[i][j - 1] = 'ПП'
    #                         if j < len(labirint[i]) - 1 and (labirint[i][j + 1] == iscomoe - 1 or labirint[i][j + 1] == 1):
    #                             labirint2[i][j + 1] = 'ПП'
    #                         print_labirint(labirint2)
    #         iscomoe -= 1

    print_labirint(labirint)
    if solve:
        print('Этот лабиринт может быть пройден')
        print('Вот так:')
        print_labirint(labirint2)
    else:
        print('Данный лабиринт не может быть пройден')

for x in range(img.size[0]):
    for y in range(img.size[1]):
        # if (x > 100 and y > 100) and (x < 600 and y < 600):
            data[x, y] = (
                255,
                255,
                255
            )

img.save('labirint2.2.png')