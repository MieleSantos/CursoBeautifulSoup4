from bs4 import  BeautifulSoup
from  bs4 import  NavigableString, Tag


with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f,'lxml')
'''
#print(soup.table.contents)
print(type(soup.contents))
print(len(soup.contents))
print(soup.table.contents[1].span)
print(soup.table.contents[1].span.string)
print(soup.table.contents[3].td)


for child in soup.table.contents:
    print(child)


for child in soup.table.contents:
    if(child.name =='tr'):
        print(child)

print(type(soup.childen))


for child in soup.footer.children:
    print(child)


#acessando os filhos diretos
for child in soup.p.footer.children:
    if(child.name=='a'):
        print(child.get('href'))

#acessando os filhos dos filhos etc
print(len(list(soup.children)))
print(len(list(soup.descendants)))
'''
for tag in soup.descendants:
    #testa se é uma string
    if(isinstance(tag, NavigableString)):
        print(tag)
    else:
        print(tag.name)



for tag in soup.descendants:
    #testa se é uma Tag
    if(isinstance(tag, Tag)):
        print(tag)
    else:
        print(tag)