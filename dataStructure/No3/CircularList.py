class ChainNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertFront(self, new):
        newNode = ChainNode(new) # ChainNode

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

    def InsertBack(self, new):
        newNode = ChainNode(new)

        if self.tail is None:
            self.tail = self.head = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode

    def IsEmpty(self):
        return self.head == None and self.tail == None

    def DeleteFront(self):
        if self.IsEmpty():
            raise Exception('Empty')

        delNode = self.head
        self.head = self.head.next
        self.tail.next = self.head

        del delNode

    def DeleteBack(self):
        if self.IsEmpty():
            raise Exception('Empty')

        delNode = self.tail
        pNode = self.head # 이전 노드

        while pNode.next is not self.tail:
            pNode = pNode.next

        pNode.next = delNode.next
        self.tail = pNode

        del delNode

    def PrintNode(self, node):
        temp = node

        while True:
            if temp.next is node:
                print(temp.data, end="")
            else:
                print(str(temp.data) + '->', end="")

            temp = temp.next
            if temp is node:
                break
        print()