# 원형 큐 : 변수 front는 큐에서 첫 원소의 위치보다 시계반대방향으로 하나 앞 위치를 가리킴
# 변수 rear는 큐에서 마지막 원소의 위치를 가리킴

class Queue:

    queue = []
    front  = 0
    rear = 0
    capacity = 10

    def __init__(self, queueCapacity = 10):
        self.capacity = queueCapacity
        self.front = self.rear = 0
        self.queue.append(0)

    def isEmpty(self):
        return self.front == self.rear

    def Front(self):
        if(self.isEmpty() == False):
            return (self.queue[(self.front + 1)] % self.capacity)

    def Rear(self):
        if(self.isEmpty() == False):
            return self.queue[self.rear]

    def Push(self, item):
        if(self.rear == self.capacity - 1):
            self.rear = 0
        self.queue.append(item)
        self.rear += 1

    def Pop(self):
        if(self.isEmpty() == False):
            self.front += 1

queue = Queue(20)
print(queue.isEmpty())
queue.Push(2)
print(queue.Front())
queue.Push(3)
queue.Push(4)
queue.Push(5)
queue.Push(6)
queue.Pop()
print(queue.Rear())
print(queue.Front())