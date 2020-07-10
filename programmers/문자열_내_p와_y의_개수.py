'''
# 문자열 내 p와 y의 개수
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
'''

def solution(s):
    s = s.lower()
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i] == 'y':
            y += 1

    if p == y:
        answer = True
    else:
        answer = False

    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))

#집계함수 사용
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution2("pPoooyY"))
print(solution2("Pyy"))