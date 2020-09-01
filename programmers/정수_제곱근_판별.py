import math
def solution(n):
    if math.sqrt(n) == round(math.sqrt(n)):
        return int(math.pow(n ** 0.5 + 1, 2))
    return -1

print(solution(121))
print(solution(3))