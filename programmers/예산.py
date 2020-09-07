def solution(d, budget):
    answer = 0
    d.sort()
    for v in d:
        if v <= budget:
            budget -= v
            answer += 1
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))