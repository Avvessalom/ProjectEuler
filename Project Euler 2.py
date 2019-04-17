n = int(input())
def fibo(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    print(f)
fibo(n)


'''def task2 ():
    a = []
    b = 0
    c = [i for i in range(1001)]
    for i in range (1002):
        a.append(a[i-1]+a[i+1])
    print(a)
task2()'''
