from first_task import Purchase
import datetime


class Order:

    def __init__(self, number: int) -> None:
        self.number = number
        self.purchases = dict()

    def __str__(self):
        return f'Номер заказа {self.number}\nСодержимое заказа: {self.purchases}'

    def add_purchase(self, purchase: Purchase, time: datetime, customer: str, address: str):
        self.purchases[purchase.title] = (purchase, time, customer, address)
        print('Покупка успешно добавлена в заказ номер {}'.format(self.number))

    def del_purchase(self, title: str):
        self.purchases.pop(title)
        print('Покупка успешно удалена из закана номер {}'.format(self.number))


my_purchase = Purchase('Молоко', 70, 50, 10)
my_order = Order(123456789)
my_order.add_purchase(my_purchase, datetime.datetime.utcnow().date(), 'Данил Федоров', 'Ул.Пушкина, Дом колотушника')
print(my_order)
my_order.del_purchase('Молоко')
print(my_order)
