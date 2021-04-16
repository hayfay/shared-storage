from math import *

count = 0
while (count < 1):
    n = input("Желаете проверить новое число? (Да/нет) ")
    if (n == 'Да' or n == 'да'):
        n = int(input("Введите число: "))
        a = n//2 + 1
        for i in range(2, a):
            if (n % i == 0):
                print(n, "- это число непростое.")
                break
        else:
            print(n, "- это простое число.")
    else:
        count = 1