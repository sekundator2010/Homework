class Cells:

    def __init__(self, numb_cell):
        self.numb_cell = numb_cell
    def __str__(self):
        return str(self.numb_cell)
    def __add__(self, other):
        return str(self.numb_cell + other.numb_cell)
    def __sub__(self, other):
        return self.numb_cell - other.numb_cell if self.numb_cell - other.numb_cell > 0 \
            else print('Операция не удовлетворяет условиям задачи')
    def __mul__(self, other):
        return str(self.numb_cell * other.numb_cell)
    def __truediv__(self, other):
        return round(self.numb_cell / other.numb_cell)
    def make_order(self, countdow):
        return '\n'.join([('*' * countdow for i in range(self.numb_cell // countdow)]) +
               '\n' + "*" * (self.numb_cell % countdow)

cell_1 = Cells(66)
print(cell_1)
print(cell_1.make_order(5))