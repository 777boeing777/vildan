class Purchase:
    def __init__(self, title, cost_rub, cost_coop, count=1):
        self.title = title
        self.cost_rub = cost_rub
        self.cost_coop = cost_coop
        self.count = count

    def total(self):

        total_rub = self.cost_rub * self.count
        print(f"Итоговая стоимость в рублях: {total_rub}")
        total_coop = self.cost_coop * self.count
        print(f"Итоговая стоимость в копейках: {total_coop}")
        total_rub_coop = (self.cost_rub + self.cost_coop / 100) * self.count
        print(f"Итоговая стоимость в копейках и рублях: {total_rub_coop}")

    def info(self):
        print(f'Товар {self.title}')
        print('Стоимость {rubs} руб. {coop} коп.'.format(rubs=self.cost_rub, coop=self.cost_coop))
        print(f'Кол-во {self.count}')


my_item = Purchase("Хлеб", 12, 50, 31)
my_item.total()
my_item.info()
