class Matrix:
    def __init__(self, b):
        self.b = b

    def __str__(self):
        return '\n'.join([','.join(map(str, st_roke)) for st_roke in self.b] )

    def __add__(self, other):
        listen = ''
        if len(self.b) == len(other.b):
            for st_roke1, st_roke2 in zip(self.b, other.b):
                sum_st_roke = [r + t for r, t in zip(st_roke1, st_roke2)]
                listen += ' '.join(map(str, sum_st_roke)) + '\n'
                return listen
        else:
            return 'Problem value'
matrix1 = Matrix([[8, 6, 4, 7], [7, 4, 9, 3], [5, 3, 4, 4], [5, 3, 2, 3]])
matrix2 = Matrix([[8, 4, 6, 4], [7, 5, 4, 3], [5, 4, 3, 8], [6, 5, 6, 3]])
print(matrix1)
print()
print(matrix1 + matrix2)
