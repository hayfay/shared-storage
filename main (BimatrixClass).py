import numpy as np
from BimatrixClass import Bimatrix

if __name__ == '__main__':
    print ('Легенда:')
    print ('\x1b[1;35m' + 'Эффективные по Парето и устойчивые по Нэшу' + '\x1b[0m')
    print ('\x1b[1;33m' + 'Эффективные по Парето' + '\x1b[0m')
    print ('\x1b[1;32m' + 'Устойчивые по Нэшу' + '\x1b[0m\n')

    game = Bimatrix()
    #решаем наш вариант
    player1 = np.array([[0, 11], [7, 6]])
    player2 = np.array([[1, 4], [8, 3]])
    game.play_game(player1, player2, 'Вариант 1', True)

    #решаем случайную игру 10x10
    N = 10
    player1, player2 = game.generate_game(N)
    game.play_game(player1, player2, '\nСлучайная игра %dx%d' % (N, N))

    #играем в перекресток
    player1 = np.array([[ -1, 0], [5, -10]])
    player2 = np.array([[-1, 5], [ 0,  -10]])
    game.play_game(player1, player2, '\nПерекресток')

    #играем в дилемму заключенных
    player1 = np.array([[-1, -10], [0, -5]])
    player2 = np.array([[-1, 0], [-10, -5]])
    game.play_game(player1, player2, '\nДилемма заключенных')

    #играем в семейный спор
    player1 = np.array([[1, 0], [0, 4]])
    player2 = np.array([[4, 0], [0, 1]])
    game.play_game(player1, player2, '\nСемейный спор')
