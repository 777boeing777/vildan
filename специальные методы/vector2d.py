class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vect2({self.x}, {self.y})'

    def __add__(self, summand):
        return Vect2(self.x + summand.x, self.y + summand.y)

    def add_vect(self, add_v):
        self.x += add_v.x
        self.y += add_v.y
        return self

    def __mul__(self, alpha):
        return self.x * alpha, self.y * alpha

    def __rmul__(self, alpha):
        return self.x * alpha, self.y * alpha

    def scale(self, alpha):
        self.x *= alpha
        self.y *= alpha
        print('Масштабирование, текущие координаты {} {}'.format(self.x, self.y))

    def vector_increment(self, other):
        self.x -= other.x
        self.y -= other.y
        print('Приращение, текущие координаты {} {}'.format(self.x, self.y))


my_vector = Vect2(1, 2)
your_vector = Vect2(2, 3)
my_vector.vector_increment(your_vector)
my_vector.scale(3)
