class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат = {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print('да нуууу....')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells):
        row = ''
        for i in range(int(self.quantity / cells)):
            row += f'{"*" * cells} \\n'
        if self.quantity % cells !=0:
            row += f'{"*" * (self.quantity % cells)}'
        else:
            row = row[:-2]
        return row

cells1 = Cell(15)
cells2 = Cell(7)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells2.make_order(5))
print(cells1.make_order(5))
