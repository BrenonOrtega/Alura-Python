from re import error
from UrlArgExtractor import UrlArgExtractor
#   Desafio Capitulo1
url = 'https://www.bytebank.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&valor=1500'

url_menor = 'https://www.bytebank.com.br/cambio?moedaOrigem=moedaDestino&moedaDestino=dolar&valor=500'

a = UrlArgExtractor(url)
b = UrlArgExtractor(url_menor)
""" moeda_origem, moeda_destino, valor = a.arg_extract()
print('*' * 50,)
print(moeda_origem, moeda_destino, valor)
print('*' * 50, '\n')

 """
print(a)

print (a == b)
