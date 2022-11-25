from bs4 import BeautifulSoup


contents = ''
with open('dom2.html', 'r', encoding='utf-8') as f:
    # contents = f.read()
    # soup = BeautifulSoup(contents, 'lxml')
    # print(soup)
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
t = soup.find_all('a')

# t2 = t.find('ul', 'rubricator-list-item-submenu-bQ0A4', recursive=False)
# t3 = t2.find_next_siblings('a')
for i in t:
    print(i)
    i2 = i.find_parent('ul')
    print(i2.)
    
    print('_______________________________________________________')

# for i in t:
#     print(i.find('ul', 'rubricator-list-item-submenu-bQ0A4'))
#     print('fffffffffffffffffffffffffffffffffffffffffff')
# print(len(t))
# print('fffffffffffffffffffffffffffffffffffffffffff')
# for i in t1:
#     print(i)
#     print('ddddddddddddddddddddddddd')

# print(len(t))

# t2 = t.find('li', 'rubricator-list-item-item-WKnEv')
# t3 = t2.find('li', 'rubricator-list-item-item-WKnEv')
# t4 = t3.find('li', 'rubricator-list-item-item-WKnEv')
# print(t4)
# id_cat = t3.ul['data-marker']
# tag_ul = t.find('ul', 'rubricator-list-item-submenu-bQ0A4')
# tag_li = t.find('li')
# print(tag_ul.name)
# t2 = t.find('li', 'rubricator-list-item-item-WKnEv')
# t3 = t2.find('li', 'rubricator-list-item-item-WKnEv')
# t4 = t3.find('li', 'rubricator-list-item-item-WKnEv')

# print(t4)
# t2 = temp[1].find_all('a')



# print('Cat:',id_cat)

# with open('temp.html', 'w', encoding='utf-8') as f:
#     for i in temp:
#         print(i)
#         f.write(str(i) + '\n')



# print(soup.head)
# print(soup.body.a)

    