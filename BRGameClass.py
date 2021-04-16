import random

class BRGame:
    def __init__(self, matrix):
        self.matrix = matrix
        self.gameTable = [[1] * 8]

    def createGameTable(self):
        a = [0] * 8
        return a

    #инициализируем первую строку таблицы
    def initGameTable(self):
        firstRow = [0] * 8
        firstRow[0] = 1
        firstRow[1] = 1
        firstRow[2] = 1
        firstRow[3] = list((x[firstRow[1] - 1] for x in self.matrix))
        firstRow[4] = self.matrix[firstRow[2] - 1]
        firstRow[5] = max(firstRow[3])
        firstRow[6] = min(firstRow[4])
        firstRow[7] = firstRow[5] - firstRow[6]
        self.gameTable.append(firstRow)

    def calculateOneStep(self, table):
        #создаем строку в таблице для следующего хода
        table.append([0] * 8)
        table[-1][0] = len(table) -1

        #находим максимально выгодный ход на предыдущем шаге
        minPrevRow = min(table[-2][4])
        maxPrevRow = max(table[-2][3])

        #если у нас несколько оптимальных ходов - выбираем из них случайный
        #максимальный
        if table[-2][3].count(maxPrevRow) > 1:
            table[-1][1] = [i for i, x in enumerate(table[-2][3]) if x == maxPrevRow]
            table[-1][1] = random.choice(table[-1][1]) + 1
        else:
            table[-1][1] = table[-2][3].index(maxPrevRow) + 1
        #минимальный
        if table[-2][4].count(minPrevRow) > 1:
            table[-1][2] = [i for i, x in enumerate(table[-2][4]) if x == minPrevRow]
            table[-1][2] = random.choice(table[-1][2]) + 1
        else:
            table[-1][2] = table[-2][4].index(minPrevRow) + 1

        #прибавляем к предыдущим результатам игроков выбранную на этом шаге стратегию
        #первый игрок
        table[-1][3] = [0] * len(table[-2][3])
        for i in range(len(table[-2][3])):
            table [-1][3][i] = table[-2][3][i] + self.matrix[i][table[-1][2] - 1]

        #второй игрок
        table[-1][4] = [0] * len(table[-2][4])
        for i in range(len(table[-2][4])):
            table [-1][4][i] = table [-2][4][i] + self.matrix[table[-1][1] - 1][i]
        #округляем полученные значения
        table[-1][5] = round(max(table[-1][3]) / table[-1][0], 2)
        table[-1][6] = round(min(table[-1][4]) / table[-1][0], 2)

        minmax = (min(list(x[5] for x in table[1:])))
        maxmin = (max(list(x[6] for x in table[1:])))
        table[-1][7] = round((minmax - maxmin), 2)

    def calculateBRGame(self):
        if len(self.gameTable) == 1:
            self.initGameTable()
        while self.gameTable[-1][7] > 0.1:
            self.calculateOneStep(self.gameTable)
        self.printBRGame()

    def printBRGame(self):
        print()
        tableHeader = ['N', 'A', 'B', 'Vector A', 'Vector B', 'AvMax', 'AvMin', 'e']
        self.gameTable[0] = tableHeader
        for i in range(len(self.gameTable)):
            a = (list(map(str, self.gameTable[i])))
            print('{:4}{:4}{:4}{:25}{:25}{:7}{:7}{:7}'.format(*a))