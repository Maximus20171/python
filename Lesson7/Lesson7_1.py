class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in self.matrix:
            for i1 in i:
                print(f'{i1:5d}', end='')
            print()
        return ' '

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
            result.append(numbers)
            numbers = []
        return Matrix(result)


m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[-11, 5], [33, - 99], [-55, 15]])
m3 = Matrix([[1, 1], [1, 1], [1, 1]])
print(m1)
print(m2)
print(m3)
print(m1+m2+m3)