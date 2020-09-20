# 합병정렬
def mergesort(S, low, high) : 
    if low < high :
        mid = (low+high) // 2
        mergesort(S, low, mid)
        mergesort(S, mid + 1, high)
        merge(S, low, mid, high)

def merge(S, low, mid, high) : 
    i = low
    j = mid + 1
    k = low
    U = []
    while i <= mid and j <= high :
        if S[i] < S[j] :
            U[k] = S[i]
            ++i
        else : 
            U[k] = S[j]
            ++j
        ++k
    if i > mid :
        n = k
        for num in range(j, high) : 
            U[n] = S[num]
            ++n
    else : 
        n = k
        for num in range(i, mid) : 
            U[n] = S[num]
    for num in range(low, high) : 
        S[num] = U[num]

S = input("배열을 입력하세요 > ")
mergesort(S, 0, len(S))
print(S)