'''
S : Single 1제곱 / D : Double 2제곱 / T : Triple 3제곱
* : 이전 점수, 현 점수 * 2 / # : 마이너스
'''

def solution(dartResult):
    num = [0, 0, 0]
    flag = -1

    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'*' : 2, '#' : -1}

    for idx, dart in enumerate(dartResult):
        if dart.isdigit():
            flag += 1
            if dart == '0':
                continue
            elif dartResult[idx + 1].isdigit(): # 10일 경우
                num[flag] = 10
                flag -= 1
            else:
                num[flag] = int(dart)

        elif dart in bonus:
            num[flag] = num[flag] ** bonus[dart]

        else:
            if dart == '*':
                num[flag-1] *= 2

            num[flag] = num[flag] * option[dart]

    return sum(num)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

# 다른 풀이
import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)