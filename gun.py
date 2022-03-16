import math


class Gun:

    def __init__(self, v, a):
        self.v = v
        self.a = a

    def max_high(self) -> float:
        return (self.v ** 2 * math.sin(math.radians(self.a)) ** 2) / (2 * 9.80665)

    def length(self) -> float:
        return (self.v ** 2 * math.sin(math.radians(2 * self.a))) / 9.80665


my_gun = Gun(100, 45)
print("Макс. высота подъёма:", my_gun.max_high(), "м.")
print("Дальность полёта:", my_gun.length(), "м.")
