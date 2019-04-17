def Palindrom(k):
    s = str(k)
    s_rev = s[::-1]
    if (s == s_rev):
        Palindrom = True
    else:
        Palindrom = False
    return Palindrom


def task4():
    a, b = [], []
    for i in range(100, 1000):
        for j in range(100, 1000):
            a.append(i*j)
    for i in range(len(a)):
        if Palindrom(a[i]) :
            b.append(a[i])
    print(max(b))


task4()
