def task3():
    taskNumber = 600851475143
    a = []
    b = []
    for i in range(2,taskNumber ):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            a.append(d)
    for i in range(len(a)):
        if taskNumber % a[i] == 0:
           b.append(a[i])
    print(max(b))


task3()