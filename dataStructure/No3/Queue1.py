# 1차원 배열 queue[]를 이용한 큐의 구현
# pop : queue[0]에 있는 원소 제거

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

    def Push(self, item):
        if(self.capacity > self.rear + 1):
            self.queue.append(item)
            self.rear += 1
        else:
            self.capacity += 10
            self.queue.append(item)
            self.rear += 1

    def Pop(self):
        if(self.isEmpty()):
            return None
        else:
            self.queue.pop(self.
