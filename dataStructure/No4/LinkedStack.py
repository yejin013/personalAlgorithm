class ChainNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedStack:

    def __init__(self):
        self.top = ChainNode(0, None)

    def Push(self, new):
        self.top = ChainNode(new, self.top)

    def Pop(self):
        if self.isEmpty():
            raise Exception('Empty')

        delNode = self.top
        self.top = self.top.next

        del delNode

    def isEmpty(self) :
        if self.top.next is None:
            return True
        else:
            return False

    def PrintAll(self):
        temp = self.top
        while True:
            if temp.next is None:
                print()
                break
            else:
                print(temp.data, end=" ")
            temp = temp.next

    def Top(self):
        return self.top.data

stack = LinkedStack()
print(stack.isEmpty())
stack.Push(2)
print(stack.Top())
stack.Push(3)
stack.Push(4)
stack.Push(5)
stack.Push(6)
stack.PrintAll()
print(stack.Pop())
print(stack.Top())