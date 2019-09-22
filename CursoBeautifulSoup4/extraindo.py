from bs4 import BeautifulSoup

with open('arquivo.html','r') as f:
    soup = BeautifulSoup(f, 'html5lib')
#formatando
print(soup.prettify())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#mostrando o texto de todas as tag
print(soup.get_text)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#conteudo das tag
print(soup.p.get_text)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#imprimindo o texxto da tag atual
print(soup.p.b.string)