import requests

#Metodo post

url='http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

payload = {'relaxation' : '12240000','tipoCep': 'ALL','semelhate': 'N'}

response = requests.post(url,data=payload)

#salvando dados em html
with open('correios.html','w') as f:
    f.write(response.text)