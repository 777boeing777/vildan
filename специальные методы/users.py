import random


class User:

    def __init__(self, name, rating=0):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return f'{self.name}, рейтинг: {self.rating}'

    def __radd__(self, summand):
        return self.rating + summand

    def __eq__(self, other):
        if self.rating == other.rating:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.rating != other.rating:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.rating > other.rating:
            return True
        else:
            return False


class UserList:
    def __init__(self, users=[]):
        self._users = users

    def __len__(self):
        return len(self._users)

    def __getitem__(self, item_number):
        return self._users[item_number]


names = [
    'Анастасия',
    'Анжела',
    'Артем',
    'Борислав',
    'Валентин',
    'Вероника'
]
users = UserList([User(name, random.randint(0, 100)) for name in names])

for user in users:
    print(user)
print('Среднее значение:', sum(users) / len(users))

print(sorted(users))
