class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Деление на ноль недопустимо"


try:
    a = float(input('Введите делитель '))
except ValueError:
    print('Не верный тип данных')
else:
    div = DivisionByNull(10, a)
    print(DivisionByNull.divide_by_null(10, a))
    print(div.divide_by_null(100, a))
