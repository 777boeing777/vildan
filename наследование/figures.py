import random
import pickle


class Figure:
    def __init__(self, side: int, high: int, **kwargs) -> None:
        self.side = side
        self.high = high
        self.other_info = kwargs

    def square(self):
        pass


class Rectangle(Figure):
    def square(self) -> float or int:
        return self.side * self.high

    def __str__(self):
        return 'Прямоугольник'


class Triangle(Figure):
    def square(self) -> float or int:
        return self.side * self.high / 2

    def __str__(self):
        return 'Треугольник'


class Circle(Figure):
    def __init__(self, radius: int) -> None:
        super().__init__(radius, radius)
        self.side = radius

    def __str__(self):
        return 'Квадрат'

    def square(self) -> float or int:
        return self.side ** 2


some = Figure(2, 3)


data = list()
for _ in range(10):

    random_figure = random.choice([Triangle, Circle, Rectangle])
    if random_figure is not Circle:
        new_figure = random_figure(random.randint(1, 10), random.randint(1, 10))
    else:
        new_figure = random_figure(random.randint(1, 10))
    data.append(new_figure)

with open('figures', 'wb') as file:
    pickle.dump(data, file)

with open('figures', 'rb') as file:
    data = pickle.load(file)

sorted_objects_list = list()
for i_object in data:
    sorted_objects_list.append(i_object)

for i in range(len(sorted_objects_list)):
    for j in range(len(sorted_objects_list)):
        if sorted_objects_list[i].square() < sorted_objects_list[j].square():
            sorted_objects_list[i], sorted_objects_list[j] = sorted_objects_list[j], sorted_objects_list[i]

for i_figure in sorted_objects_list:
    print(f'{i_figure}, площадь: {i_figure.square()}')
