class Fractions:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.float_num = self.numerator / self.denominator

    def __str__(self):
        return rf'{self.numerator}/{self.denominator}'

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value: int):
        if value != 0:
            self._denominator = value
        else:
            raise ZeroDivisionError('Знаменатель не может быть равен 0')

    def __lt__(self, other: 'Fractions'):
        if self.float_num  < other.float_num:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.float_num == other.float_num:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.float_num != other.float_num:
            return True
        else:
            return False

    def __add__(self, other: int):
        return self.float_num + other

    def __radd__(self, other):
        return self.float_num + other

    def __mul__(self, other):
        return self.float_num * other

    def __rmul__(self, other):
        return self.float_num * other

    def __sub__(self, other):
        return self.float_num - other

    def __rsub__(self, other):
        return self.float_num - other

    def __truediv__(self, other):
        return self.float_num / other

    def __rtruediv__(self, other):
        return other / self.float_num


my_num = Fractions(3, 4)
your_num = Fractions(3, 4)
print(my_num / 4)
