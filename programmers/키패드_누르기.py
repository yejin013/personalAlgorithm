def distance(number, hand):
    location = {'1':(0, 0), '2':(0, 1), '3':(0, 2),
                '4':(1, 0), '5':(1, 1), '6':(1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand-x_number) + abs(y_hand-y_number)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'

    if hand == 'left':
        hand = 'L'
    else:
        hand = 'R'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = str(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            right = str(num)
        elif num in [2, 5, 8, 0]:
            disLeft = distance(num, left)
            disRight = distance(num, right)

            if disLeft > disRight:
                answer += 'R'
                right = str(num)
            elif disLeft < disRight:
                answer += 'L'
                left = str(num)
            else:
                answer += hand
                if hand == 'R':
                    right = str(num)
                else:
                    left = str(num)

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))