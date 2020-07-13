# 다항식

class Term:
    coef = 0.0 # 계수
    exp = 0 # 지수

    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp

class Polynomial:
    termArray = []
    capacity = 0
    terms = 0

    def __init__(self, termArray = Term(0, 0), terms = 0):
        self.termArray = termArray
        self.capacity = len(self.termArray)
        self.terms = terms

    def NewTerm(self, coef, exp):
        if self.terms == self.capacity:
            self.capacity *= 2
        self.termArray.append(Term(coef, exp))
        # self.termArray[self.terms].coef = coef
        # self.termArray[self.terms].exp = exp
        self.terms += 1

    def Add(self, b):
        aPos = 0
        bPos = 0
        c = Polynomial()

        while((aPos < self.terms) & (bPos < b.terms)):
            if (self.termArray[aPos].exp) == (b.termArray[bPos].exp):
                t = self.termArray[aPos].coef + b.termArray[bPos].coef
                if t:
                    c.NewTerm(t, self.termArray[aPos].exp)
                    aPos += 1
                    bPos += 1
            elif (self.termArray[aPos].exp) < (b.termArray[bPos].exp):
                c.NewTerm(b.termArray[bPos].coef, b.termArray[bPos].exp)
            else:
                c.NewTerm(self.termArray[aPos].coef, self.termArray[aPos].exp)

        for _ in range(aPos, self.terms):
            c.NewTerm(self.termArray[aPos].coef, self.termArray[aPos].exp)

        for _ in range(aPos, self.terms):
            c.NewTerm(b.termArray[bPos].coef, b.termArray[bPos].exp)

        return c

array = []
array.append(Term(3, 2))
array.append(Term(2, 1))
array.append(Term(-1, 0))
poly = Polynomial(array, 0)

b = []
b.append(Term(1, 8))
b.append