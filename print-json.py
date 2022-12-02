import json


loads = ''

with open('category-lv.json', 'r', encoding='utf-8') as f:
    loads = f.read()

cat_dict = json.loads(loads)   # получаем словарь {"имя категории": ["id категори, id родителя"]}
from pprint import pprint 
pprint(cat_dict)