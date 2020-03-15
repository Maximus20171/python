class StoreMashines:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        #self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'Введите наименование ')
            unit_p = float(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_unit}')
        except:
            print(f'Ошибка ввода данных')
        finally:
            print(f'Для выхода - Q, продолжить заполнять - Enter')
            q = input(f'---> ')
            if q.lower() == 'q':
                self.my_store_full.append(self.my_store)
                print(f'Весь склад -\n {self.my_store_full}')
                return f'Выход'
            else:
                return StoreMashines.reception(self)


class Printer(StoreMashines):
    def __init__(self, name, price, quantity, formatA='A4'):
        super().__init__(name, price, quantity)
        self.formatA= formatA

    def to_print(self):
         return f'Список принтеров {self.my_store_full}' if self.my_store_full != [] else 'На складе нет принтеров'


class Scanner(StoreMashines):
    def __init__(self, name, price, quantity, formatA='A4'):
        super().__init__(name, price, quantity)
        self.formatA= formatA

    def to_scan(self):
        return f'Список сканеров {self.my_store_full}' if self.my_store_full != [] else 'На складе нет сканеров'


class Copier(StoreMashines):
    def __init__(self, name, price, quantity, formatA='A4'):
        super().__init__(name, price, quantity)
        self.formatA= formatA

    def to_copier(self):
        return f'Список копиров {self.my_store_full}' if self.my_store_full != [] else 'На складе нет ксерексов'


unit_1 = Printer('hp', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Copier('Xerox', 1500, 1)
store=0
while store==0:
    try:
        store = int(input('Что будем заполнять: 1)Printer 2)Scanner 3)Copier '))
        if store==1:
            print('Составляем список принторов')
            unit_1.reception()
        if store==2:
            print('Составляем список сканеров')
            unit_2.reception()
        if store==3:
            print('Составляем список ксероксов')
            unit_3.reception()
        else:
            print('от 1-3')
    except:
        store = 0
        print('не верные данные')

print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())