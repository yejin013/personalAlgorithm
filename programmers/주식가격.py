'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''

def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer

print(solution([1, 2, 3, 2, 3]))