def summ(n):
    i = 0
    s = 1
    for i in range(n):
        a = int(input())
        s = s * a
    print(s)

h = int(input('Введите количство множителей'))
summ(h)
