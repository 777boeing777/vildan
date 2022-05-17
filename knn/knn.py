import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split

from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


iris = datasets.load_iris()
X, y = iris.get('data'), iris.get('target')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Здесь просто разделяем данные
                                                                                          # на тренировочные и тестовые

# ---------Не обязательно, просто если интересно посмотреть на расположение данных------------
# cmap = ListedColormap(['#FF0000', "#00FF00", '#0000FF'])
# plt.figure()
# plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap, edgecolors='k', s=20)
# plt.show()
# --------------------------------------------------------------------------------------------

class KNN:
    def __init__(self, k=3):
        self.k_ = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        distances = [self.calculate_distance(x, x_train) for x_train in self.X_train] # считаем расстояния
        k_indices = np.argsort(distances)[:self.k_] # сортируем наши расстояния и получаем три наиболее ближайших
        k_nearest_labels = [self.y_train[i] for i in k_indices]  # достаём эти ближайшие данные по индексам
        most_common = Counter(k_nearest_labels).most_common(1) # получаем наиболее распространенные значения
        return most_common[0][0]

    def calculate_distance(self, x1, x2):
        return np.sqrt(np.sum(x1 - x2) ** 2)


knn = KNN()
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test) # проверяем насколько мы правильно угадаали
print(acc)
