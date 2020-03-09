class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self, pos):
        if pos == self.position:
            fio = self.name + ' ' + self.surname
        return print('Фамилия Имя: ', fio)

    def get_total_income(self):
        summa = sum((self.__dict__.get('_income')).values())
        return print('Доход =', summa)


p = Position('Иван', 'Иванович','Бригадир', 60000, 10000)
p.get_full_name('Бригадир')
p.get_total_income()
