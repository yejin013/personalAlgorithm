def solution(n):
    return sum(int(i) for i in str(n))

print(solution(123))
print(solution(987))

def solution2(n):
    answer = 0

    while n:
        answer += n % 10
        answer //= 10

    return answer