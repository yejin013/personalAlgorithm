def solution(s):
    temp = s.split(' ')
    answer = ''
    for i in temp:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer

print(solution("try hello world"))

# 예시
def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

print(toWeirdCase("try hello world"))