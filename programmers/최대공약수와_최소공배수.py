# 유클리드 호제법으로 풀기
def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer

def gcd(a, b):
    while (b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


print(solution(3, 12))
print(solution(2, 5))