class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa_a(self, tol):
        self.tol = tol
        return print('Масса необходимого асфальта ', self._length * self._width * 25 * self.tol / 1000)


r = Road(20, 5000)
r.massa_a(5)
