class Stationery:
    def __init__(self, title):
        self.title=title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки ручки {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки карандаша {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки Маркера {self.title}')

pen = Pen('Parker')
pencil = Pencil('IKEY')
handle = Handle('Красный')
pen.draw()
pencil.draw()
handle.draw()