'''
Программа парсить категории авито. Для начала необходимо сохранить страницу 
одной из корневых категорий авито. На выходе json файл формата: {<название категории>: [id_old, id_parent_old]}
id_old, id_parent_old - это id категории и id родителя на сайте авито
'''
import json
from bs4 import BeautifulSoup


contents = ''
with open('lv.html', 'r', encoding='utf-8') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
block_category = soup.find('div', class_='rubricator-root-SshbP')   # вырезаем блок категорий
tags_a = block_category.find_all('a')   # забираем все теги "a"
data = {}

for a in tags_a:
    ul_parent = a.find_parent('ul')   # для каждого тега "a" обращаемся к родителю "ul"
    name = a.string   # имя категории
    id_old = a.get('data-marker')[:-5]   # id категории
    id_parent_old = ul_parent.get('data-marker')[:-5]   # id категории родителя
    data[name] = [id_old, id_parent_old]
    print(f'{name} / {id_old} / {id_parent_old}')


with open("category-lv.json","w") as file:   # записываем в json файл 
    json.dump(data, file)

