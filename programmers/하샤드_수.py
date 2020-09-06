def solution(x):
    d = sum(int(i) for i in str(x))
    if x % d == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))