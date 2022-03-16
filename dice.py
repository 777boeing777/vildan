import random


class Dice:
    __count = 0

    @classmethod

    def cast(cls) -> None:
        Dice.__count += 1
        first_dice, second_dice = random.randint(1, 6), random.randint(1, 6)
        print(f'Бросок № {Dice.__count}')
        print(f'Очки на первом и втором кубике соответственно ({first_dice};{second_dice})')
        print(f'Сумма очков броска {first_dice + second_dice}\n')


my_dice = Dice()
for _ in range(10):
    my_dice.cast()
