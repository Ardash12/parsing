from bs4 import BeautifulSoup


contents = ''
with open('dom.html', 'r', encoding='utf-8') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
t = soup.find('li')

for a in t:
    print(a.find_parent('ul'))
    print('_' * 12)
    print(a)
    print('_' * 12)