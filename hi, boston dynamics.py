class Robot:
    def __init__(self, x_coordinate, y_coordinate, orient):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.orient = orient
        self.__way = list()

    def __logging(self, current_place: tuple) -> None:
        self.__way.append(current_place)

    @property
    def orient(self):
        return self._orient

    @orient.setter
    def orient(self, orient):
        if orient in range(0, 3):
            self._orient = orient
        else:
            print('Выбрано неверное направление.')


    def move(self, steps: int) -> None:
        if self.orient == 0:
            self.x_coordinate += steps
        elif self.orient == 1:
            self.y_coordinate += steps
        elif self.orient == 2:
            self.x_coordinate -= steps
        else:
            self.y_coordinate -= steps
        self.__logging((self.x_coordinate, self.y_coordinate))

    def print_path(self):
        print(self.__way)

    def way_length(self):
        length_x = 0
        length_y = 0
        for i_point in self.__way:
            length_x += i_point[0]
            length_y += i_point[1]

        length = (length_x ** 2 + length_y ** 2) ** (1 / 2)
        return length


my_robot = Robot(0, 0, 0)
my_robot.move(5)
my_robot.move(2)
my_robot.orient = 1
my_robot.move(2)
my_robot.move(4)
print(f"{my_robot.way_length():.2f}")
my_robot.print_path()
