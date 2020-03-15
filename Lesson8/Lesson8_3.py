class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        y_or_n, i = 'y', 1
        while y_or_n != 'n' and i == 1:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')
                if y_or_n.lower() == 'y':
                    i = 0
                    try_except.my_input()
                else:
                    y_or_n = 'n'
        return f'ИТОГОВЫЙ СПИСОК {self.my_list}'


try_except = Error()
print(try_except.my_input())
