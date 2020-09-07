def solution(n, arr1, arr2):
    answer = []
    c_arr1 = []
    c_arr2 = []
    for v1, v2 in zip(arr1, arr2):
        c_arr1.append(format(v1, "0"+str(n)+"b"))
        c_arr2.append(format(v2, "0"+str(n)+"b"))
    value = ''
    for v1, v2 in zip(c_arr1, c_arr2):
        for i1, i2 in zip(v1, v2):
            if (i1 == '1') or (i2 == '1'):
                value += '#'
            else:
                value += ' '
        answer.append(value)
        value = ''
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))