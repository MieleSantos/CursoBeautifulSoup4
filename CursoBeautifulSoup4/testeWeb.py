import requests
from bs4 import  BeautifulSoup

'''
with open('arquivo.html','r') as f:
    soup_string = BeautifulSoup(f.read(),'html.parser')
    print(soup_string)'''

''''
r = requests.get('http://www.google.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)'''


'''
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

#exibindo tudo que tem na tag title titulo da pagina'''
'''
tag = soup.title
print(tag)
print(tag.name)'''
#exibindo tudo que tem na tag p
'''
tag = soup.p
print(tag)
print(tag.name)
'''
#acessando o atributo class da tag p

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.p['class'])

#mostrando os atributos da tag p

print(soup.p.attrs)

#recuperando o link da tag a
#o acesso aos atributos e feito usando dicionarios ou get
print(soup.a['href'])
print(soup.a.get('href'))



