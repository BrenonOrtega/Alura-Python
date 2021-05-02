#Trabalhando com dados em python
dados = {"Jetta Variant": 50_000, "Passat": 75_000, "CrossFox": 60_000}
print(dados)

#criando listas
valores = list()
for valor in dados.values():
    valores.append(valor)
print (valores)

#Pode ser resumido por isso:
lista = list(dados.values())
print(lista)

#somando valores
soma = sum(dados.values())
print(soma)

##################################################################
#Funções com dicts e lists.

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_por_ano_medio(dataset, ano_atual):
    return [(key, item['km']/(ano_atual-item['ano'])) for key, item in dataset.items()]
    
ano = 2019
media_km = km_por_ano_medio(dados, ano)
print(media_km)


#Refatorando a função para atualizar o dataset com as médias calculadas
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

#Adicionando novos campos a um dict.
def km_por_ano_medio2(dataset, ano_atual):
    for key, item in dataset.items():
        dataset[key].update({"Média": item['km']/ (ano_atual-item['ano'] ) } )
    return dataset

print(km_por_ano_medio2(dados, 2019), )


