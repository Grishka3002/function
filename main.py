import math

def umn():
    i = 0
    a = int(input('Введите множитель. Для завершения введите -0 '))
    s = a
    while i == 0:
        a = int(input())
        if a == -0:
            break
        else:
            s = s * a
    print(s)
    
def sum():
    i = 0
    a = int(input('Введите слагаемое. Для завершения введите -0 '))
    s = a
    while i == 0:
        a = int(input())
        if a == -0:
            break
        else: 
            s = s + a
    print(s)

def delit():
    i = 0
    a = int(input("Введите число, которое нужно разделить. "))
    s = a
    while i == 0:
        a = int(input("Введите число на которое нужно разделить. Для завершения введите -0 "))
        if a == -0:
            if (s*10) % 10 != 0:
                h = int(input("Определите точность вычесления (кол-во цифр после запятой)"))
            break
        else:
            s = s/a
    print(round(s, h))

def minus():
    i = 0
    a = int(input('Введите уменьшаемое. '))
    s = a
    while i == 0:
        a = int(input("Введите число которое вычетаем. Для завершения введите -0 "))
        if a == -0:
            break
        else: 
            s = s - a
    print(s)

def fuct():
    i = 0
    while i == 0:
        a = int(input("Введите число факториал которого нужно вычислить. Для завершения введите -0 "))
        s = 1
        if a == -0:
            break
        for c in range(2, a+1):
            s = s*c
        print(s)

t = 1
while t == 1:
    d = input("Выберите действие, которое хотите совершить. 1 - умножение, 2 - сложение, 3 - деление, 4 - вычетание, 5 - факториал . ")
    if d == "1":
        umn()
        break
    elif d == "2":
        sum()
        break
    elif d == "3":
        delit()
        break
    elif d == "4":
        minus()
        break
    elif d == "5":
        fuct()
        break
    else:
        print("Выберите одно из предложеных действий")
