from scipy.special import factorial

coalitions = (set(), {1}, {2}, {3}, {4},
    {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
    {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4})


def vector(v):
    if v == {0}:
        return 0
    elif v == {1}:
        return 4
    elif v == {2}:
        return 1
    elif v == {3}:
        return 3
    elif v == {4}:
        return 1
    elif v == {1, 2}:
        return 6
    elif v == {1, 3}:
        return 8
    elif v == {1, 4}:
        return 6
    elif v == {2, 3}:
        return 5
    elif v == {2, 4}:
        return 3
    elif v == {3, 4}:
        return 5
    elif v == {1, 2, 3}:
        return 9
    elif v == {1, 2, 4}:
        return 8
    elif v == {1, 3, 4}:
        return 10
    elif v == {2, 3, 4}:
        return 7
    elif v == {1, 2, 3, 4}:
        return 11
    return 0


def check_superadditivity():
    print('Проверка на супераддиктивность:')
    for el1 in coalitions:
        for el2 in coalitions:
            if not el1 & el2 and not vector(el1 | el2) >= vector(el1) + vector(el2):
                print('Не является супераддиктивной, так как при S={0}, T={1} v(S U T)={2} < v(S) + v(T)={3}'.format(el1, el2, vector(el1|el2),vector(el1)+vector(el2)))
                return False

    print('Является супераддитивной\n')
    return True


def check_convexity():
    print('Проверка на выпуклость:')
    for el1 in coalitions:
        for el2 in coalitions:
            if not vector(el1 | el2) + vector(el1 & el2) >= vector(el1) + vector(el2):
                print('Игра не является выпуклой, так как при S={0}, T={1} v(S U T)+v(S ∩ T)={2} < v(S)+v(T)={3} \n'.format(el1, el2, vector(el1 | el2) + vector(el1 & el2), vector(el1) + vector(el2)))
                return False

    print('Игра является выпуклой\n')
    return True


def find_Shapley():
    X = []
    N = 4
    for i in range(1, 5):
        x_i = sum([factorial(len(S) - 1) * factorial(N - len(S)) * (vector(S) - vector(S - {i}))
                   for S in coalitions if i in S]) / factorial(N)
        X.append(x_i)
    my = []
    for i in X:
        my.append(float('{:.3f}'.format(i)))
    my=str(my)
    print('Вектор Шепли: ' + my + '\n')

    if sum(X) == vector({1, 2, 3, 4}):
        print('Условие групповой рационализации выполняется')
    else:
        print('Условие групповой рационализации не выполняется')

    try:
        for i in range(1, 5):
            if not X[i - 1] >= vector({i}):
                raise Exception('Не выполняется')

        print('Условие индивидуальной рационализации выполняется')
    except Exception as e:
        if str(e) == 'Не выполняется':
            print('Условие индивидуальной рационализации не выполняется')

if __name__ == "__main__":
    check_superadditivity()
    check_convexity()
    find_Shapley()