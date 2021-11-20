class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        for i in self.m:
            print(i)
        return ''

    def __add__(self, other):
        for i in range(len(self.m)):
            for j in range(len(other.m[i])):
                self.m[i][j] = self.m[i][j] + other.m[i][j]
        return Matrix.__str__(self)


m1 = Matrix([[1, 2, 3],
             [3, 4, 5],
             [6, 7, 8]])

m2 = Matrix([[-2, 0, 2],
             [-2, 0, 2],
             [0, 2, -2]])

print(m1)
print(m2)
print(m1.__add__(m2))
