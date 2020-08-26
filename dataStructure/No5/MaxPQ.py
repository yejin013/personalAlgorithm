# 우선순위 큐 : 가장 값이 큰 원소부터 제거
class MaxPQ:
    pq = []

    def isEmpty(self):
        if len(self.pq) == 0:
            True
        else:
            False

    def push(self, data):
        self.pq.append(data)

    def top(self):
        max = 0

        for x in self.pq:
            if max < x:
                max = x

        return max

    def pop(self):
        max = 0

        for i in range(len(self.pq)): # i는 index
            if self.pq[max] < self.pq[i]:
                max = i

        self.pq.pop(max)

    def all(self):
        print(self.pq)

pq = MaxPQ()
pq.push(3)
pq.push(5)
pq.push(1)
pq.push(2)
print(pq.top())
pq.pop()
pq.all()
print(pq.top())
pq.pop()
print(pq.top())