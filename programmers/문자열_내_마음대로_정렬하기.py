'''
# 문자열 내 마음대로 정렬하기
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
'''

def solution(strings, n):
    if n != 0:
        for i in range(len(strings)):
            for j in range(i, len(strings)):
                if strings[i][n] > strings[j][n]:
                    strings[i], strings[j] = strings[j], strings[i]
                elif strings[i][n] == strings[j][n]:
                    if strings[i] > strings[j]:
                        strings[i], strings[j] = strings[j], strings[i]
    else:
        strings = sorted(strings)
    return strings

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))

# 간단한 버전
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]
print(strange_sort(strings, 1))
print(strange_sort(strings2, 2))