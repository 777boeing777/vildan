class Interval:
    def __init__(self, start: int or float, end: int or float):
        self.a = start
        self.b = end

    def __add__(self, other: 'Interval'):
        return self.a + other.a, self.b + other.b

    def __radd__(self, other: 'Interval'):
        return self.a + other.a, self.b + other.b

    def __mul__(self, other: 'Interval'):
        return (min(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b),
                max(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b))

    def __rmul__(self, other: 'Interval'):
        return (min(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b),
                max(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b))

    def __sub__(self, other: 'Interval'):
        return self.a - other.b, self.b - other.a

    def __rsub__(self, other: 'Interval'):
        return other.a - self.b, other.b - self.a

    def __truediv__(self, other: 'Interval'):
        return (min(self.a / other.a, self.a / other.b, self.b / other.a, self.b / other.b),
                max(self.a / other.a, self.a / other.b, self.b / other.a, self.b / other.b))

    def __rtruediv__(self, other: 'Interval'):
        return (min(other.a / self.a, other.a / self.b, other.b / self.a, other.b / self.b),
                max(other.a / self.a, other.a / self.b, other.b / self.a, other.b / self.b))


my_interval = Interval(1, 4)
your_interval = Interval(4, 6)
print(my_interval * your_interval)
print(my_interval / your_interval)
print(my_interval - your_interval)
print(my_interval + your_interval)
