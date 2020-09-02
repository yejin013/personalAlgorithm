def solution(arr):
    return (sum(arr) // len(arr) if sum(arr) // len(arr) == sum(arr) / len(arr) else sum(arr) / len(arr))

print(solution([1, 2, 3, 4]))
print(solution([5, 5]))