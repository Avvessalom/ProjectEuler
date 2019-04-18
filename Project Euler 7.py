def problem7():
    taskNumber = 10001               #int(input())
    a = []
    for i in range(2,100000000):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            a.append(d)
        if len(a) == taskNumber:
            break
    print(a[taskNumber-1])


problem7()
