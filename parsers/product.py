__author__ = 'verbalist'

from EF import db

class Product():

    def __init__(self, name, energy_price):
        self.name = name
        self.protein = energy_price[0]
        self.fat = energy_price[1]
        self.carbon = energy_price[2]
        self.calories = energy_price[3]


import requests
from bs4 import BeautifulSoup
r = requests.get('http://diet-calc.ru/eatbase/')
b = BeautifulSoup(r.text)
mas = [x.text for x in b.find_all('td', attrs={'class': 'TablesContent'})]
# mas = [x if x not in mas[:i] + mas[:i + 1] else x + '1' for i, x in enumerate(mas)]
mas1 = []
mas2 = []
for i, x in enumerate(b.find_all('td', attrs={'class': 't_right'})):
    if (i + 1) % 4 == 0:
        mas2.append(x.text)
        mas1.append(Product(mas[int((i + 1)/4 - 1)], mas2))
        mas2 = []
    else:
        mas2.append(x.text)

for x in mas1:
    try:
        db.execute('insert into product(fat, carbon, name, protein, calories) values' + '(' + ','.join(
    [x.fat, x.carbon, '\''+ x.name[:62] + '\'', x.protein, x.calories])+')')
    except Exception as e:
        print(e)
        db.execute('insert into product(fat, carbon, name, protein, calories) values' + '(' + ','.join(
            [x.fat, x.carbon, '\''+ x.name[:62] + '1\'', x.protein, x.calories])+')')


# print([x.__dict__ for x in mas1])
# print('insert into product(fat, carbon, name, protein, calories) values' + ','.join(['(' + ','.join(
#     [x.fat, x.carbon, x.name, x.protein, x.calories])+')' for x in mas1]))