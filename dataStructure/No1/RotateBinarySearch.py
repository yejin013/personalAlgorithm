# 순환 이원 탐색 : 정렬된 리스트에서 key 값 찾기
## 입력값 : 리스트, key

def RotateBinarySearch(list, key, left, right):
    middle = int((left + right)/2)
    if(left <= right):
        if key < list[middle]:
            return RotateBinarySearch(list, key, left, middle - 1)
        elif key > list[middle]:
            return RotateBinarySearch(list, key, middle + 1, right)
        elif key == list[middle]:
            return middle
    else:
        return -1

def SelectionSort(a, n):
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

n = int(input('배열 크기 : '))
list = list()
for i in range(n):
    list.append(int(input()))
key = int(input('찾고자 하는 키 : '))

list = SelectionSort(list, n) # 정렬
left = 0
right = n - 1
print(RotateBinarySearch(list, key, left, right))