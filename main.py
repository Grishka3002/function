def summ():
    i = 0
    s = 0
    a = int(input('Введите слагаемое. Для завершения введите -0'))
    s = a
    while i == 0:
        a = int(input())
        if a == -0:
            break
        else: 
            s = s + a
    print(s)

def umn():
    i = 0
    s = 1
    a = int(input('Введите множитель. Для завершения введите -0'))
    s = a
    while i == 0:
        a = int(input())
        if a == -0:
            break
        else:
            s = s * a
    print(s)

t = 1
while t == 1:
    d = input("Выберите действие, которое хотите совершить. 1 - умножение, 2 - сложение.")
    if d == "1":
        umn()
        break
    elif d == "2":
        summ()
        break
    else:
        print("Выберите одно из предложеных действий")
