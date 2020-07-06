# 선택 정렬
def SelectionSort(a, n):
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

list = list()
num = int(input()) # 리스트 크기 입력
for i in range(num):
    new = int(input())
    list.append(new)

print(SelectionSort(list, num))