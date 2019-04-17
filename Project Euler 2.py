def task2(n):
    f = [0, 1]
    for i in range(2, n + 1):
            f.append(f[i-1] + f[i-2])
            if f[i] > 4000000:
                del f[i]
                break
    print(f)
    a = 0
    for i in range(len(f)):
        if f[i]%2 == 0:
            a += f[i]
    print(a)


task2(100)

