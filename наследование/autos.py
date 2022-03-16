class Auto:
    def __init__(self, model: str, max_speed: int):
        self.model = model
        self.max_speed = max_speed

    def print_info(self):
        print(f'Модель машины: {self.model}\nМаксимальная скорость: {self.max_speed}')


class Bus(Auto):
    def __init__(self, model: str, max_speed: int, seats_count: int):
        super().__init__(model, max_speed)
        self.seats_count = seats_count
        self.current_seats = 0

    def print_info(self):

        return f'Автобус {self.model}, максимальная скорость - {self.max_speed},' \
               f' кол-во мест - {self.seats_count}'

    def bus_stop(self, stop: 'BusStop'):
        print(f'Рассаживаем людей в автобус {self.model}...\n')
        if self.current_seats + stop.people_counts <= self.seats_count:
            self.current_seats += stop.people_counts
            print(f'Остановка, зашли {stop.people_counts} людей,'
                  f' осталось {self.seats_count - self.current_seats} мест в автобусе {self.model}.')
            stop.people_counts = 0
        else:
            stop.people_counts -= self.seats_count - self.current_seats
            print(f'Зашло {self.seats_count - self.current_seats} людей')
            self.current_seats = self.seats_count
            print(f'Мест в автобусе {self.model} больше нет, остальные {stop.people_counts} людей ждут следюущего')


class Truck(Auto):
    def __init__(self, model: str, max_speed: int, weight: int, max_cargo: int):
        super().__init__(model, max_speed)
        self.weight = weight
        self.max_weight = max_cargo

    def print_info(self):
        return f'Грузовик {self.model}, максимальная скорость - {self.max_speed},' \
               f' вес - {self.weight}, максимальный груз - {self.max_weight}'

    def put_in_truck(self, cargo: 'Cargo'):
        print(f'Загружем в грузовик {self.model}...\n')
        if self.weight + cargo.weight <= self.max_weight:
            self.weight += cargo.weight
            print(f'В автобус {self.model} положили новый груз весом {cargo.weight} кг,'
                  f' осталось места на {self.max_weight - self.weight} кг')
            cargo.weight = 0
        else:
            cargo.weight -= self.max_weight - self.weight
            self.weight = self.max_weight
            print(f'Грузовик {self.model} полностью загружен, осталось груза на {cargo.weight}кг.')


class Cargo:
    def __init__(self, weight: int):
        self.weight = weight


class BusStop:
    def __init__(self, people_counts: int):
        self.people_counts = people_counts


class AutoPark:
    def __init__(self, bus_count: tuple = None, trucks_count: tuple = None):
        self.buses = bus_count
        self.trucks = trucks_count

    def print_info(self):
        print(f'В нашем автопарке есть {len(self.buses)} автобусов и {len(self.trucks)} грузовиков.\n')
        buses_info = ''
        for i_bus in self.buses:
            buses_info = f'{buses_info}{i_bus.print_info()}\n'
        print(f'Информация по автобусам:\n{buses_info}')
        trucks_info = ''
        for i_truck in self.trucks:
            trucks_info = f'{trucks_info}{i_truck.print_info()}\n'
        print(f'Информация по грузовикам:\n{trucks_info}')

    def transport_cargo(self, cargo: Cargo):
        max_cargo = 0
        for i_truck in self.trucks:
            max_cargo += i_truck.max_weight
        if cargo.weight <= max_cargo:
            print(f'Автопарк начал загружаться.\n')
            for i_truck in self.trucks:
                i_truck.put_in_truck(cargo)
                if cargo.weight == 0:
                    print('Весь груз полностью загружен')
                    break
        else:
            print(f'Недостаточно грузовиков')

    def transport_people(self, stops: BusStop):
        max_people = 0
        for i_bus in self.buses:
            max_people += i_bus.seats_count
        if max_people >= stops.people_counts:
            print(f'Автобус поехал.')
            for i_bus in self.buses:
                i_bus.bus_stop(stops)
                if stops.people_counts == 0:
                    print('Больше людей на остановках не осталось')
                    break
        else:
            print(f'Недостаточно автобусов')


truck_1 = Truck(model='Мерседес-бенз', max_speed=100, weight=150, max_cargo=2000)
truck_2 = Truck(model='Лада', max_speed=90, weight=120, max_cargo=1200)
bus_1 = Bus(model='Русская тройка', max_speed=120, seats_count=70)
bus_2 = Bus(model='Красный двухэтажный', max_speed=100, seats_count=120)

my_park = AutoPark((bus_1, bus_2), (truck_1, truck_2))

cargo = Cargo(2500)
people_count = BusStop(150)
#my_park.transport_cargo(cargo)
my_park.transport_people(people_count)
