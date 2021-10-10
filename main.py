def summ(n):
    i = 0
    s = 0
    for i in range(n):
        a = int(input())
        s = s + a
    print(s)

def umn(n):
    i = 0
    s = 1
    for i in range(n):
        a = int(input())
        s = s * a
    print(s)

d = input("Выберите действие, которое хотите совершить. 1 - умножение, 2 - сложение.")
if d == "1":
    h = int(input('Введите количство множителей'))
    umn(h)
else:
    h = int(input('Введите количство слагаемых'))
    summ(h)
