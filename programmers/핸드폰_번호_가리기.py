def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    answer += phone_number[-4:]
    return answer

print(solution("01033334444"))
print(solution("0277778888"))