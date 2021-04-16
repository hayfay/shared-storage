from fractions import Fraction
import copy

def solve_simplex(mtrx, varlist):
    stage1 = True #Флаг окончания этапа 1
    stage2 = True #Флаг окончания этапа 2
    n = len(mtrx) #Количество строк симплекс-таблицы
    m = len(mtrx[0]) #Количество столбцов симплекс-таблицы
    r = -1 #Номер разрешающей строки
    k = -1 #Номер разрешающего столбца
    answer = {'error1': 'None', #Ошибка на 1-м этапе
            'error2': 'None', #Ошибка на 2-м этапе
            'mtrx1': [], #Промежуточные симплек-таблицы этапа 1
            'rk1': [],
            'mtrx2': [], #Промежуточные симплек-таблицы этапа 2
            'rk2': [] }
    #Первоначальная симплекс таблица
    addmtrx1 = copy.deepcopy(mtrx)
    addmtrx1.insert(0, varlist[0])
    for i in range(0, n):
        addmtrx1[i+1].insert(0, varlist[1][i])
    answer['mtrx1'].append(addmtrx1)
    answer['rk1'].append([r, k])
    #Этап №1. Поиск опорного решения
    while(stage1):
        stage1 = False
        for i in range(n-1):
            #Поиск отрицательного элемента в столбце свободных членов
            if mtrx[i][0] < 0:
                stage1 = True
                #Поиск разрешающего столбца
                for j in range(1, m):
                    if mtrx[i][j]<0:
                        k = j
                        break
                #Если не нашли отрицательного элемента, то решений нет
                else:
                    answer['error1'] = 'Нет допустимых решений.'
                    return answer
                #Поиск разрешающей строки
                searchlist = []
                for a in range(n-1):
                    if mtrx[a][k]!=0:
                        searchlist.append(mtrx[a][0] / mtrx[a][k])
                    else:
                        searchlist.append(-1)
                r = sorted([(index, value) for (index, value) in enumerate(searchlist) if value > 0], key=lambda x: x[1])[0][0]
                #Замена переменных
                temp = varlist[0][k]
                varlist[0][k] = varlist[1][r]
                varlist[1][r] = temp
                newmtrx = [[0 for a in range(m)] for b in range(n)]
                #Пересчёт симплекс-таблицы
                for x in range(n):
                    for y in range(m):
                        if (x!=r and y!=k):
                            newmtrx[x][y] = mtrx[x][y] - mtrx[x][k] * mtrx[r][y] / mtrx[r][k]
                        elif (x==r and y!=k):
                            newmtrx[x][y] = mtrx[r][y] / mtrx[r][k]
                        elif (x!=r and y==k):
                            newmtrx[x][y] = - mtrx[x][k] / mtrx[r][k]
                        elif (x==r and y==k):
                            newmtrx[x][y] = 1 / mtrx[x][y]
                mtrx = newmtrx
                addmtrx = copy.deepcopy(mtrx)
                addmtrx.insert(0, varlist[0])
                for i in range(0, n):
                    addmtrx[i+1].insert(0, varlist[1][i])
                answer['mtrx1'].append(addmtrx)
                answer['rk1'].append([r, k])
                break
    #Этап №2. Поиск оптимального решения
    while(stage2):
        stage2 = False
        for j in range(1, m):
            #Поиск разрешающего столбца
            if mtrx[n-1][j] > 0:
                stage2 = True
                k = j
                for i in range(n-1):
                    if mtrx[i][k] > 0:
                        break
                else:
                    answer['error2'] = 'Не существует оптимального решения.'
                    return answer
                #Поиск разрешающей строки
                searchlist = []
                for a in range(n-1):
                    if mtrx[a][k]!=0:
                        searchlist.append(mtrx[a][0] / mtrx[a][k])
                    else:
                        searchlist.append(-1)
                r = sorted([(index, value) for (index, value) in enumerate(searchlist) if value > 0], key=lambda x: x[1])[0][0]
                #Замена переменных
                temp = varlist[0][k]
                varlist[0][k] = varlist[1][r]
                varlist[1][r] = temp
                newmtrx = [[0 for a in range(m)] for b in range(n)]
                #Пересчёт симплекс-таблицы
                for x in range(n):
                    for y in range(m):
                        if (x!=r and y!=k):
                            newmtrx[x][y] = mtrx[x][y] - mtrx[x][k] * mtrx[r][y] / mtrx[r][k]
                        elif (x==r and y!=k):
                            newmtrx[x][y] = mtrx[r][y] / mtrx[r][k]
                        elif (x!=r and y==k):
                            newmtrx[x][y] = - mtrx[x][k] / mtrx[r][k]
                        elif (x==r and y==k):
                            newmtrx[x][y] = 1 / mtrx[x][y]
                mtrx = newmtrx
                addmtrx = copy.deepcopy(mtrx)
                addmtrx.insert(0, varlist[0])
                for i in range(0, n):
                    addmtrx[i+1].insert(0, varlist[1][i])
                answer['mtrx2'].append(addmtrx)
                answer['rk2'].append([r, k])
                break
    return answer
