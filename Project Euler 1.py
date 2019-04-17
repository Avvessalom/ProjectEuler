def task1 ():
    summ = 0
    a = [i for i in range (1001)]
    for i in range(1000):
        if a[i]%3 == 0 or a[i]%5 == 0:
            summ += a[i]
    print(summ)
task1()
