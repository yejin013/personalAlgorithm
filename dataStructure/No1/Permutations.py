# 순열 생성기 : ㅁ[k],...a[m]에 대한 모든 순열 생성
# 입력값 : 문자 여러 개

def swap(k, i):
    temp = k
    k = i
    i = temp
    return k, i

def Permutations(a, k, m):
    if k == m:
        for i in range(m + 1):
            print(a[i], end='')
        print()

    else:
        for i in range(k, m + 1):
            a[k], a[i] = swap(a[k], a[i])
            Permutations(a, k+1, m)
            a[k], a[i] = swap(a[k], a[i])

n = int(input('배열 크기 : '))
a = list()
for i in range(n):
    a.append(input())

Permutations(a, 0, n-1)