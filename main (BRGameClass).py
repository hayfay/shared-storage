from BRGameClass import BRGame

def enterData():
    path = input('---- Привет ! ----\nВведите путь до файла со вводными данными: ')
    matrix = [list(map(float, (x.split()))) for x in open(path, 'r').readlines()]
    matrix= matrix[1:]
    return matrix


def __main__():
    matrix = enterData()
    newGame = BRGame(matrix)
    newGame.calculateBRGame()


__main__()