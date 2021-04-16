from functools import *

def vipolnenie():
    global schet2
    global key
    global i2
    global i3
    if schet2 == 0:
        vibor = int(input ("\nКакую операцию желаете выполнить? \n 1) Сложение \n 2) Перемножение \n 3) Среднее арифметическое \n"))
    else:
        vibor = int(input("\nКакую операцию желаете выполнить? \n 1) Сложение \n 2) Перемножение \n 3) Среднее арифметическое \n 4) Добавить элементы \n 5) Удалить элементы \n"))
    if vibor == 1:
        schet2 = 1
        answer1 = reduce(lambda res, x: res + x, list, 0)
        print("\n Сумма =", summ(*list), '=', answer1)
    if vibor == 2:
        schet2 = 1
        answer2 = reduce(lambda res, x: res * x, list, 1)
        print("\n Перемножение =", umn(*list), '=', answer2)
    if vibor == 3:
        schet2 = 1
        answer3 = reduce(lambda res, x: res + x, list, 0)
        print("\n Среднее арифметическое ", arifm(*list), '=', answer3/len(list))
    if vibor == 4 and schet2 == 1:
        schet2 = 1
        i2 = 0
        quantity = int(input("Введите количество: "))
        while i2 < quantity:
            list.append(int(input(" Введите %s число: " % dict[key + i2 + 1])))
            i2 += 1
    elif vibor == 4 and schet2 != 1:
        print("\nОшибка! Повторите выбор \n")
        vipolnenie()
    if vibor == 5 and schet2 == 1:
        schet2 = 1
        i3 = 0
        x = 1
        quantity = int(input("Введите количество: "))
        udal = []
        while i3 < quantity:
            udal.append(int(input(" Введите номер удаляемого элемента: ")))
            i3 += 1
        udal.sort()
        for i in udal:
            del list[i - x]
            x += 1
    elif vibor == 5 and schet2 != 1:
        print("\nОшибка! Повторите выбор \n")
        vipolnenie()
    if vibor > 5 or vibor < 1:
        print("\nОшибка! Повторите выбор \n")
        vipolnenie()
    key = len(list)

def summ(*args):
    global itog
    sobr = []
    schet = 1
    for i in args:
        i = str(i)
        sobr.append(i)
        if schet != len(list):
            sobr.append("+")
        schet += 1
    itog = func2(*sobr)
    return itog

def umn(*args):
    global itog
    sobr = []
    schet = 1
    for i in args:
        i=str(i)
        sobr.append(i)
        if schet!=len(list):
            sobr.append("*")
        schet += 1
    itog = func2(*sobr)
    return itog

def arifm(*args):
    global itog
    sobr = []
    schet = 1
    sobr.append("(")
    for i in args:
        i = str(i)
        sobr.append(i)
        if schet != len(list):
            sobr.append("+")
        schet += 1
    sobr.append(")/%s" % len(list))
    itog = func2(*sobr)
    return itog

def func2(*sobr):
    sobr2 = ''.join(sobr)
    return sobr2

#############################################################################

key = 0
i2 = 0
i3 = 0
schet2 = 0
sum = []
dict = {1:"первое", 2:"второе", 3:"третье", 4:"четвёртое", 5:"пятое", 6:"шестое", 7:"седьмое", 8:"восьмое", 9:"девятое", 10:"десятое",
        11:"одиннадцатое", 12:"двенадцатое", 13:"тринадцатое", 14:"четырнадцатое", 15:"пятнадцатое", 16:"шестнадцатое", 17:"семнадцатое",
        18:"восемнадцатое", 19:"девятнадцатое", 20:"двадцатое", 21:"двадцать первое", 22:"двадцать второе", 23:"двадцать третье"}
list = [] # хранит весь набор чисел
quantity = int(input("Введите количество: "))
while key < quantity:
    if key >= 23:
        list.append(int(input(" Введите следующее число: ")))
    else:
        list.append(int(input(" Введите %s число: " % dict[key+1])))
    key += 1
vipolnenie()
vibor2 = int(1)
while int(vibor2) <= 2:
    sobr = []
    for k in list:
        sobr.append(str(k))
    print("------------------------------- \n \nЭлементы: %s" % ', '.join(sobr), ".")
    vibor2 = input("\nЧто-нибудь ещё? \n 1) Да \n 2) Нет \n")
    if vibor2 == '1':
        vipolnenie()
    elif vibor2 == '2':
        print ("Спасибо")
        vibor2 = 3
    else:
        print("\nОшибка! Повторите выбор \n")
        vibor2 = 0
