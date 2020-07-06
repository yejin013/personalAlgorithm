'''
# 완주하지 못한 선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

# 정확도 통과, 효율성 실패
import copy
def solution(participant, completion):
    answerlist = copy.deepcopy(participant)
    for i in participant:
        if i in completion:
            answerlist.remove(i)
            completion.remove(i)
    answer = answerlist[0]
    return answer

participant1 = ["leo", "kiki", "eden"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion1 = ["eden", "kiki"]
completion2  = ["josipa", "filipa", "marina", "nikola"]
completion3 = ["stanko", "ana", "mislav"]

solution1 = solution(participant1, completion1)
solution2 = solution(participant2, completion2)
solution3 = solution(participant3, completion3)

print(solution1)
print(solution2)
print(solution3)

# 정확도 통과, 효율성 통과
def solutionPC(p, c):
    p.sort()
    c.sort()

    for par, com in zip(p, c):
        if par != com:
            return par
    return p[-1]

participant1 = ["leo", "kiki", "eden"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion1 = ["eden", "kiki"]
completion2  = ["josipa", "filipa", "marina", "nikola"]
completion3 = ["stanko", "ana", "mislav"]

print(solutionPC(participant1, completion1))
print(solutionPC(participant2, completion2))
print(solutionPC(participant3, completion3))

'''
# key point
zip을 사용하는 것이 좋다는 점
zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
'''