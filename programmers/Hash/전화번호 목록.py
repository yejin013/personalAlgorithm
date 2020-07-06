'''
# 전화번호 목록
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
'''

# 정확도 통과, 효율성 실패
def solution(phone_book):
    phone_book.sort()
    answer = True

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                answer = False

    return answer

phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123", "456", "789"]
phone_book3 = ["12", "123", "1235", "567", "88"]

print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))

# 정확도 통과, 효율성 통과
def solutionPB(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solutionPB(phone_book1))
print(solutionPB(phone_book2))
print(solutionPB(phone_book3))