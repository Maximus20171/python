from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def square_c(self):
        pass

    @abstractmethod
    def square_s(self):
        pass

    @property
    def __add__(self, other):
        return f'Общая площадь {round((float(Coat.square_c())+float(Suit.square_s())),2)}'


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def __str__(self):
        return f'Площадь на пальто {self.V}'

    def square_c(self):
        return round(self.V / 6.5 + 0.5, 2)

    def square_s(self):
        pass


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def __str__(self):
        return f'Площадь на костюм {self.H}'

    def square_c(self):
        pass

    def square_s(self):
        return round(self.H * 2 + 0.3,2)


my_coat = Coat(7)
my_suit = Suit(4)
print('Площадь ткани на костюм', my_suit.square_s())
print('Площадь ткани на пально', my_coat.square_c())
print('Общая площадь',my_coat.square_c()+my_suit.square_s())