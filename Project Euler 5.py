def task5():
    n = 0
    b = 0
    while b != 20:
        n += 1
        b = 0
        for i in range(1, 21):
            if n % i == 0:
                b += 1
    print(n)


task5()