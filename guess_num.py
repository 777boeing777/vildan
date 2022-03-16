import random


class GuessNumber\
:
    def __init__(self):
        self.level = 1

    @classmethod
    def start_game(cls):
        print('Добро пожаловать в игру "Угадай-Число"!\nn'
              'Игра разделена на три уровня:\n'
              '1 уровень - компьютер загадывает число от 0 до 5\n'
              '2 уровень - компьютер загадывает число от 0 до 10\n'
              '3 уровень - компьютер загадывает число от 0 до 25\n'
              'Выберите уровень, используя метод choose_level.')

    def choose_level(self, level):
        if level in (1, 2, 3):
            self.level = level
            print('Уровень успешно установлен, guess - для перехода в игру.')
        else:
            print('Некорректное значение.')

    def guess(self, number):
        if self.level == 1:
            guess_number = random.randint(0, 5)
        elif self.level == 2:
            guess_number = random.randint(0, 10)
        else:
            guess_number = random.randint(0, 25)

        if number == guess_number:
            print('Вы угадали! Примите наши поздравления!')
        else:
            print('Вы не угадали! Примите наши соболезнования!')


game = GuessNumber()
game.start_game()
game.choose_level(1)
game.guess(1)
