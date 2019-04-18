def problem6():
    c = 0
    b = 0
    a =[i**2 for i in range(1, 101)]
    for i in range(100):
        c += a[i]
    for i in range(1, 101):
        b += i
    b **= 2
    print(b-c)


problem6()
