class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + self.b * other.a}*i'

    def __str__(self):
        return f'z = {self.a} + {self.b}*i' if self.b >= 0 else f'z = {self.a} {self.b}*i'


z_1 = ComplexNumber(7, 3)
z_2 = ComplexNumber(5, -8)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
