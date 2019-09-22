import requests
from bs4 import BeautifulSoup


url ='http://michaelis.uol.com.br/busca?'

playload={'r':'0','f':'0','t':'0','palavra':'talk'}

r = requests.get(url, params=playload)

soup = BeautifulSoup(r.text,'lxml')
div = soup.find('div',{'id': 'content'})

print(div.get_text())
with open('michaelis.html','w', encoding='utf-8') as f:
    f.write(r.text)
