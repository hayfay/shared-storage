import numpy as np

class Bimatrix:
    def __init__(self):
        self.a =1

    def play_game(self, player1, player2, game_name, flag=False):
        pareto = self.find_pareto(player1, player2)
        nash = self.find_nash(player1, player2)
        print(game_name)
        print('Матрица игры:')
        self.printGame(player1, player2, pareto, nash)
        if (len(nash) == 2 and flag):
            x1 = ((player2[1][1] - player2[1][0]) / (player2[0][0] + player2[1][1] - player2[1][0] - player2[0][1]))
            y1 = ((player1[1][1] - player1[0][1]) / (player1[0][0] + player1[1][1] - player1[1][0] - player1[0][1]))
            x2 = ((player2[0][0] - player2[0][1]) / (player2[0][0] + player2[1][1] - player2[1][0] - player2[0][1]))
            y2 = ((player1[0][0] - player1[1][0]) / (player1[0][0] + player1[1][1] - player1[1][0] - player1[0][1]))

            v1 = ((player1[0][0] * player1[1][1] - player1[0][1] * player1[1][0]) /
                  (player1[0][0] + player1[1][1] - player1[1][0] - player1[0][1]))
            v2 = ((player2[0][0] * player2[1][1] - player2[0][1] * player2[1][0]) /
                  (player2[0][0] + player2[1][1] - player2[1][0] - player2[1][0]))
            print("\nСмешанные стратегии")
            x1 = round(x1, 3)
            y1 = round(y1, 3)
            x2 = round(x2, 3)
            y2 = round(y2, 3)
            v1 = round(v1, 3)
            v2 = round(v2, 3)
            print("Первый игрок: ("+str(y1)+","+str(y2)+")" + "\nВторой игрок: ("+str(x1)+","+str(x2)+")")
            print("v1 = " + str(v1) + "\nv2 = " + str(v2))

    def find_pareto(self, player1, player2):
        N = np.shape(player1)[0]
        def more_effective(i1, j1, i2, j2):
            return (i1, j1) != (i2, j2) and player1[i1][j1] >= player1[i2][j2] and player2[i1][j1] >= player2[i2][j2]
        pareto = set()
        for i in range(N):
            for j in range(N):
                is_pareto = True
                for k in range(N):
                    for l in range(N):
                        if more_effective(k, l, i, j):
                            is_pareto = False
                if is_pareto:
                    pareto.add((i, j))
        return pareto

    def find_nash(self, player1, player2):
        max_A = set()
        argmax = np.argmax(player1, axis=0)
        for i, max in enumerate(argmax):
            max_A.add((max, i))
        max_B = set()
        for j, max in enumerate(np.argmax(player2, axis=1)):
            max_B.add((j, max))
        return max_B & max_A


    def generate_game(self, N):
        player1 = np.random.randint(low=10, high=99, size=(N, N))
        player2 = np.random.randint(low=10, high=99, size=(N, N))
        return (player1, player2)

    def printGame(self, player1, player2, pareto, nash):
        N = np.shape(player1)[0]
        for i in range(N):
            row = ''
            for j in range(N):
                if ( (i, j) in pareto) and ( (i, j) in nash ):
                    row += '\x1b[1;35m' + ' ('+ str(player1[i][j]) + ',' + str(player2[i][j]) + ') ' + '\x1b[0m'
                elif ( (i, j) in pareto):
                    row += '\x1b[1;33m' + ' ('+ str(player1[i][j]) + ',' + str(player2[i][j]) +') ' + '\x1b[0m'
                elif ((i, j) in nash):
                    row += '\x1b[1;32m' + ' ('+ str(player1[i][j]) + ',' + str(player2[i][j]) + ') ' + '\x1b[0m'
                else:
                    row += '\x1b[0m' + ' ('+ str(player1[i][j]) + ',' + str(player2[i][j]) + ')' + '\x1b[0m'
            print(row)