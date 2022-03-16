class Apple():
    def __init__(self, x: int, y: int, r: float or int) -> None:
        self.x_coordinate = x
        self.y_coordinate = y
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r: int or float):
        if isinstance(r, int or float):
            self._radius = r
        else:
            print('Введите целое число.')

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x: int):
        if isinstance(x, int):
            self._x_coordinate = x
        else:
            print('Введите целое число.')

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y: int):

        if isinstance(y, int):
            self._y_coordinate = y
        else:
            print('Введите целое число.')

    def __str__(self):
        return f'Координаты x, y - ({self.x_coordinate};{self.y_coordinate}), радиус - {self.radius}'

    def is_cross(self, other: 'Apple'):
        centre_distance = ((self.y_coordinate - other.y_coordinate) ** 2
                           + (self.x_coordinate - other.x_coordinate) ** 2) ** (1/2)
        if centre_distance > self.radius + other.radius:
            print('Яблоки не пересекаются')
        else:
            print('Есть пересечение')


my_apple = Apple(1, 2, 3)
your_apple = Apple(4, 5, 1)
my_apple.is_cross(your_apple)
