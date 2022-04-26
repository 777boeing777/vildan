import numpy as np
from bs4 import BeautifulSoup
import requests
import json

url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets"
items_array = np.array([])

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
info = soup.find_all('div', class_='row ecomerce-items ecomerce-items-ajax')
items = info[0].get('data-items')
items = json.loads(items)
prices_array = np.array([])
for i_item in items:
    items_array = np.append(items_array, {'title': i_item.get('title'),
                                          'description': i_item.get('description'),
                                          'price': float(i_item.get('price'))})
    prices_array = np.append(prices_array, float(i_item.get('price')))
average_price = prices_array.mean()

print(f'Максимальная цена: {prices_array.max()}')
print(f'Минимальная цена: {prices_array.min()}')
print(f'Средняя цена: {average_price}')
print()
for i_item in items_array:
    if i_item.get('price') > average_price:
        print(f'Цена на {i_item.get("title")} выше среднего и стоит {i_item.get("price")}')
    else:
        print(f'Цена на {i_item.get("title")} ниже среднего и стоит {i_item.get("price")}')
