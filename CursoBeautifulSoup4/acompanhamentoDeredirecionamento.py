import requests

r = requests.get('http://www.google.com')
#para permite o redirecionamento allow_redirects=True
r = requests.get('http://www.google.com', allow_redirects=False)
print(r.url)
#cabeçalho do redirecionamento da url
print(r.history[0].headers)