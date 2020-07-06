'''
# 모의고사
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''

def solution(answers):
    answer1 = [1, 2, 3, 4, 5] * 2000
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    count = [0, 0, 0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            count[0] += 1
        if answers[i] == answer2[i]:
            count[1] += 1
        if answers[i] == answer3[i]:
            count[2] += 1

    for i in range(3):
        if count[i] == max(count):
            answer.append(i + 1)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))