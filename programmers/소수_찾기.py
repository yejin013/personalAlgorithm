'''
# 소수 찾기
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
'''
# 에라토스테네스의 체 이용
def solution(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(2*i, n+1, i):
                sieve[j] = False

    return len([i for i in range(2, n+1) if sieve[i] == True])

print(solution(10))
print(solution(5))

# set 이용
def solution2(n):
    sieve = set(range(2,n+1))

    for i in range(2,n+1):
        if i in sieve:
            sieve -= set(range(2*i,n+1,i))
    return len(sieve)

print(solution2(10))
print(solution2(5))