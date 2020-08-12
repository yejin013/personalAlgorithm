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
        return self.stack[0]

    def Push(self, item):
        self.stack.append(item)

    def Pop(self):
        return self.stack.pop(0)

stack = Stack(20)
print(stack.isEmpty())
stack.Push(2)
print(stack.Top())
stack.Push(3)
stack.Push(4)
stack.Push(5)
stack.Push(6)
print(stack.Pop())
print(stack.Top())