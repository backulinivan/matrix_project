class Matrix:

    def __init__(self, lines, columns):
        if type(lines) != int or type(columns) != int or lines <= 0 or columns <= 0:
            raise ValueError()
        else:
            self.lines = lines
            self.columns = columns
            self.matr = [[0 for i in range(columns)] for j in range(lines)]


    def printMatrix(self):
        for i in range(self.lines):
            for j in range(self.columns):
                print(self.matr[i][j], end=' ')
            print('\n')

    def get_m(self):
        return self.lines

    def get_n(self):
        return self.columns

    def get_size(self):
        return((self.lines, self.columns))

    def get(self, i, j):
        return self.matr[i][j]

    def __add__(self, other):
        res = Matrix(self.lines, self.columns)
        for i in range(self.lines):
            for j in range(self.columns):
                res.matr[i][j] = self.matr[i][j] + other.matr[i][j]
        return res

    def __sub__(self, other):
        res = Matrix(self.lines, self.columns)
        for i in range(self.lines):
            for j in range(self.columns):
                res.matr[i][j] = self.matr[i][j] - other.matr[i][j]
        return res

    def set(self, i, j, value):
        self.matr[i][j] = value

    def __eq__(self, other):
        if self.lines != other.lines or self.columns != other.columns:
            raise RuntimeError()
        return self.matr == other.matr

    def transpose(self):
        res = Matrix(self.columns, self.lines)
        for i in range(self.columns):
            for j in range(self.lines):
                res.matr[i][j] = self.matr[j][i]
        return res

    def __mul__(self, other):
        res = Matrix(self.lines, self.columns)
        if type(other) == float or type(other) == int:
            res.matr = [[self.matr[i][j] * other for j in range(self.columns)] for i in range(self.lines)]
        else:
            if self.columns != other.lines:
                raise RuntimeError()
            else:
                res = Matrix(self.lines, other.columns)
                for i in range(self.lines):
                    for j in range(other.columns):
                        for k in range(self.columns):
                            res.matr[i][j] += self.matr[i][k] * other.matr[k][j]

    def __truediv__(self, other):
        res = Matrix(self.lines, self.columns)
        res.matr = [[self.matr[i][j] / other for j in range(self.columns)] for i in range(self.lines)]
        return res

m1 = Matrix(3, 2)
m2 = Matrix(3, 2)
Matrix.printMatrix(m1)
Matrix.printMatrix(Matrix.__add__(m1, m2))
