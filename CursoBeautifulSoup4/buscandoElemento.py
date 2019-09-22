from bs4 import BeautifulSoup

with open('arquivo04.html','r') as f:
    soup = BeautifulSoup(f,'lxml')

#procurando por tag
'''
tag = soup.find('li')
print(tag)'''

#procurando por texto
'''
tag = soup.find(string='plants')
print(tag)'''

#procurando pelo id
'''
tag = soup.find(id='secondaryconsumers')
print(tag)'''

#busca baseado classe css
'''
tag = soup.find(attrs={'class':'primaryconsumerlist'})
print(tag)'''

#usando mais de um filtro
'''
tag=soup.find('li',attrs={'class':'producerlist'})
print(tag)

tag = soup.ul.li.find('li')
print(tag)


def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumers = soup.find(is_secondary_consumers)
print(secondary_consumers.li.div.string)'''

#Buscando elementos com find_all
""""
tag_list=soup.find_all('ul')
print(tag_list)

tag_list =soup.find_all(['ul','div'])
print(tag_list)"""

#limitando por ocorrencia
'''
tag_list = soup.find_all('ul',limit=2)
print(tag_list)
'''
tag_list = soup.find_all(string =True)
print(tag_list)

tag_list = soup.find_all(string=['rabbit','bear'])
print(tag_list)

tag_list=soup.find_all(class_=['producerlist','primaryconsumerlist'])
print(tag_list)

tag_list = soup.ul.find_all('div')
print(tag_list)

tag_list = soup.find_all('div',class_='name')
print(tag_list)