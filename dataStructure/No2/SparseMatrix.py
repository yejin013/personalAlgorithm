# 희소행렬

class MatrixTerm:
    row = 0
    col = 0
    value = 0

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

class SparseMatrix:
    rows = 0
    cols = 0
    terms = 0
    capacity = 0
    smArray = []

    def __init__(self, row, col, value):
        self.smArray = MatrixTerm(row, col, value)

    def transpose(self, cols, rows, terms):
        b = SparseMatrix(cols, rows, terms)

        if terms > 0:
            currentB = 0
            for c in range(0, cols):
                for i in range(0, terms):
                    if self.smArray[i].col == c:
                        b.smArray[currentB].row = c
                        b.smArray[currentB].col = self.smArray[i].row
                        b.smArray[currentB].value = self.smArray[i].value
                        currentB += 1
        return b



