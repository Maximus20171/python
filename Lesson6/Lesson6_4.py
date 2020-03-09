class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.n = 8  # Направление. 8- вперед

    def go(self):
        self.speed = 10
        print("Заводим автомобиль")

    def stop(self):
        self.speed = 0
        print("Останавливаем работу двигателя")

    # Направление задется на правой части клавиатуры кнопками право/влево... они же цифры
    def direction(self, turn):
        my_turn = {4: 'налево', 6: 'направо', 8: 'вперед', 2: 'назад'}
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            print('Теперь мы едим', my_turn.get(turn))
            self.n = turn
        else:
            print('Текущее направление', my_turn.get(self.n))

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.speed}. ВНИМАНИЕ: Скорость ограниченна 60 ')
        else:
            print(f'Текущая скорость {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        #print(self.speed)
        if self.speed > 40:
            print(f'Текущая скорость {self.speed}. ВНИМАНИЕ: Скорость ограниченна 40 ')
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        pass

c = Car(70, 'red', 'Masda', False)
c.direction(4)
c.direction(6)
c.direction(0)
c.show_speed()
w = WorkCar(60, 'red', 'Пожарная', False)
w.show_speed()
w.direction(6)
p =PoliceCar(40, 'White', 'Police')
print(p.is_police)
p.direction(4)
p.show_speed()
p.go()
p.show_speed()