# 중위 표기에서 후위 표기로
class Stack:
    stackCapacity = 10
    stack = []
    def __init__(self, stackCapacity = 10):
        self.stackCapacity = stackCapacity

    def isEmpty(self) :
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Top(self):
        return self.stack[-1]

    def Push(self, item):
        self.stack.append(item)

    def Pop(self):
        return self.stack.pop()

def Postfix(e) :
    stack = Stack()
    result = []
    operator = {'+':2, '-':2, '*':1, '/':1}

    for x in e:
        if x == '(':
            stack.Push(x)
        elif x == ')':
            while True:
                if stack.Top() == '(':
                    stack.Pop()
                    break
                else:
                    result.append(stack.Pop())
        elif x not in operator:
            result.append(x)
        else:
            if stack.isEmpty() == False and stack.Top() in operator:
                for i in operator:
                    if stack.Top() == i:
                        a = operator[i]
                    if x == i:
                        b = operator[i]
                if a > b:
                    stack.Push(x)
                elif a == b:
                    result.append(stack.Pop())
                    stack.Push(x)
                else:
                    result.append(x)
            else:
                stack.Push(x)

    while True:
        if stack.isEmpty():
            break
        else:
            result.append(stack.Pop())

    print(result)

eval = input('중위표기식 : ')
Postfix(eval)