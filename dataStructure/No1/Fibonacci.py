# 피보나치 수열 생성

def Fibonacci(n):
    if n <= 1:
        print(n)
    else:
        fnm2 = 0
        fnm1 = 1
        for i in range(2, n + 1):
            fn = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = fn
            print(fn, end=' ')
        print()
        print(n, '번째 :', fn)

n = int(input("피보나치 수열 n : "))
Fibonacci(n)