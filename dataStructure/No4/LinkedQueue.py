class ChainNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.rear = ChainNode(0, 0)
        self.front = ChainNode(0, self.rear)
        self.chain = 0

    def isEmpty(self):
        if self.chain == 0:
            return True
        else:
            return False

    def Front(self):
        return self.front.next.data

    def Rear(self):
        return self.rear.data

    def Push(self, new):
        if self.isEmpty():
            self.rear = ChainNode(new, 0)
            self.front.next = self.rear
            self.chain += 1
        else:
            self.rear.next = ChainNode(new, 0)
            self.rear = self.rear.next
            self.chain += 1

    def Pop(self):
        if self.isEmpty():
            raise Exception('Empty')

        delNode = self.front.next
        self.front.next = self.front.next.next

        self.chain -= 1

        del delNode

    def PrintAll(self):
        temp = self.front.next

        while True:
            if temp == self.rear:
                print(temp.data)
                break
            else:
                print(temp.data, end=" ")
            temp = temp.next

queue = LinkedQueue()
print(queue.isEmpty())
queue.Push(2)
print(queue.Front())
queue.Push(3)
queue.Push(4)
queue.Push(5)
queue.Push(6)
queue.Pop()
queue.PrintAll()
print(queue.Rear())
print(queue.Front())