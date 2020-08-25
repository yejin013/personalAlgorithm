class TreeNode:

    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

class Tree:

    def __init__(self):
        self.root = None

    def Put(self, data):
        if self.root:
            self._put(data, self.root)
        else:
            self.root = TreeNode(data)

    def _put(self, data, currentNode):
        if data < currentNode.data:
            if currentNode.hasLeftChild():
                self._put(data, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(data)
        else:
            if currentNode.hasRightChild():
                self._put(data, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(data)

    # 중위 순회
    def Inorder(self, currentNode):
        if currentNode is not None:
            self.Inorder(currentNode.leftChild)
            self.Visit(currentNode)
            self.Inorder(currentNode.rightChild)

    # 전위 순회
    def Preorder(self, currentNode):
        if currentNode is not None:
            self.Visit(currentNode)
            self.Preorder(currentNode.leftChild)
            self.Preorder(currentNode.rightChild)

    # 후위 순회
    def Postorder(self, currentNode):
        if currentNode is not None:
            self.Postorder(currentNode.leftChild)
            self.Postorder(currentNode.rightChild)
            self.Visit(currentNode)

    # 출력
    def Visit(self, currentNode):
        print(currentNode.data)

myTree=Tree()
myTree.Put(3)
myTree.Put(2)
myTree.Put(5)
myTree.Put(4)
myTree.Put(1)

print("inorder")
myTree.Inorder(myTree.root)
print("preorder")
myTree.Preorder(myTree.root)
print("postorder")
myTree.Postorder(myTree.root)