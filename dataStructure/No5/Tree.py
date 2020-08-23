class TreeNode:
    data = 0
    leftChild = 0
    rightChild = 0

    def __init__(self, data, leftChild, rightChild):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

class Tree:

    def __init__(self, data, leftChild, rightChild):
        self.root = TreeNode(data, leftChild, rightChild)

    def Inorder(self):
        self.Inorder(self.root)

    def Inorder(self, currentNode):
        if currentNode.data != 0:
            self.Inorder(currentNode.leftChild)
            self.Visit(currentNode)
            self.Inorder(currentNode.rightChild)

    def Preorder(self):
        self.Preorder(self.root)

    def Preorder(self, currentNode):
        if currentNode.data != 0:
            self.Visit(currentNode)
            self.Preorder(currentNode.leftChild)
            self.Preorder(currentNode.rightChild)

    def Postorder(self):
        self.Postorder(self.root)

    def Postorder(self, currentNode):
        if currentNode.data != 0:
            self.Postorder(currentNode.leftChild)
            self.Postorder(currentNode.rightChild)
            self.Visit(currentNode)

    # 출력
    def Visit(self, currentNode):
        print(currentNode)