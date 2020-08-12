# 변수 front를 사용하여 큐의 첫번째 위치를 항상 유지
# pop : queue[front]에 있는 원소 제거

class Queue:

    queue = []
    front  = 0
    rear = 0
    capacity = 10

    def __init__(self, queueCapacity = 10):
        self.capacity = queueCapacity
        self.front = self.rear = 0

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def Front(self):
        return self.queue[self.front]

    def Rear(self):
        return self.queue[self.rear - 1]

    def Push(self, item):
        if(self.capacity > self.rear + 1):
            self.queue.append(item)
            self.rear += 1
        else:
            self.capacity += 10
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