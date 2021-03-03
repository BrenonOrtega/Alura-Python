# Curso de python voltado para data science e pandas básico.

[INSERIR TUDO QUE ESTÁ DISTRIBUIDO EM VÁRIAS PASTAS E PROJETOS AGORA]

### [Python built-in functions](https://docs.python.org/3.6/library/functions.html)

#### type()

Dá a definição do tipo de objeto passado no argumento.

#### zip(iterator1, iterator2, ... iteratorn)

A função zip retorna um objeto do tipo zip, que a cada iteravel passado como argumento, terá seus index unidos, sendo que o tamanho do iterador (zip) será decidido a partir do iterável com menor comprimento.

#### help(function)
A função help(function) é muito boa para entender alguma função do python, invocando ela do terminal, será mostrado a documentação com alguns exemplos relacionados a função, estrutura ou biblioteca passada, caso exista.

### Pandas

Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.

Dentre essas estruturas de dados, temos por exemplo as series, arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas de uma series são conhecidos como index, e temos abaixo a forma básica de criação dessa estrutura:

```python

```

```python
s = pd.Series(dados, index = index)
```

Aqui estamos chamando a biblioteca Pandas por meio de seu apelido pd seguido de Series(), para o qual passamos os dados e um index (quando necessário). Esse argumento dados pode ser um dicionário, uma lista, um array Numpy ou uma constante.

Também temos o Dataframe, uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Assim como as series, os dataframes são capazes de armazenar qualquer tipo de dado.

```python
df = pd.DataFrame(dados, index = index, columns = columns)
```

#### Criando dataframes e arrays numpy

A propriedade T é uma forma de acessar o método transpose() do DataFrame.
ndarray.T: Retorna o array transposto, isto é, converte linhas em colunas e vice versa.

```python
import pandas as pd

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })
    return result

carros = pd.DataFrame(km_media(dados, 2019)).T
'''
            km          ano     km_media
Crossfox    35000.0     2005.0  2500.0
DS5         17000.0     2015.0  4250.0
Fusca       130000.0    1979.0  3250.0
Jetta       56000.0     2011.0  7000.0
Passat      62000.0     1999.0  3100.0
'''
```

## Tipos de dados no pandas

### Criando Dataframes

Ao importarmos um arquivo com a função pd.read_csv(), também podemos passar um parâmetro "index_col = 0", definindo a coluna que desejamos assumir como índice do dataframe.

```python
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
```

caso estejamos criando um dataframe com dados próprios, podemos definir qual será o index através da função ".set_index()"

```python
data = {
    "cor": ["azul", "laranja", "preto"],
    "preço": [5000, 15000, 15000],
    "carro": ['escort', 'civic', 'ka'],
    "ano de fabricação": [1998, 2005, 2008]
}

df = pd.DataFrame(data=data)
df = df.set_index("carro")

'''
Output:

        cor     preço   ano de fabricação
carro       
escort  azul    5000    1998
civic   laranja 15000   2005
ka      preto   15000   2008

'''
```

### pandas.DataFrame.head()

A função .head() do pandas serve para mostrar oss cinco primeiros registros do nosso conjunto de dados, dando uma "amostra" do que é o nosso dataset.

Se quisermos selecionar somente a coluna "Valor", por exemplo, bastará passarmos o seu rótulo entre colchetes.

```python
dataset['Valor']
```

Um DataFrame nada mais é que um conjunto de series agrupadas, para recebermos apenas um dos dados do dataframe sem recebê-lo como uma series, ou seja, ainda com os index agrupados, para acessar um elemento de uma lista usamos o operador de indexação [], portanto para receber este dado como um dataframe e não apenas como uma Series devemos passar os campos que desejamos dentro de dois colchetes "[[]]".
Exemplo:

```python
ds[["Valor"]]
'''
output:
                        Valor
Nome
Jetta Variant           88078.64
Passat                  106161.94
Crossfox                72832.16
DS5                     124549.07
Aston Martin DB4        92612.10
... ... ... ... ... ... ... ... 
Phantom 2013            51759.58
Cadillac Ciel concept   51667.06
Classe GLK              68934.03
Aston Martin DB5        122110.90
Macan                   90381.47
258 rows × 1 columns
'''
```

Selecionar linhas de maneira simples funciona da mesma maneira que em listas, tuplas e arrays Numpy, passando os index dentro dos colchetes.

```python
dataset[0] #retorna toda a série de dados da linha 0 do dataset
```

Também é possível realizar os fatiamentos (slicing) dentro dessa indexação, lembrando que o primeiro index é inclusivo e o segundo index é exclusivo.

```python
dataset[1:5] 
'''
retorna toda a série de dados referentes as linhas 1 
até a linha 4 do dataset (a linha 5 não é incluída).
'''
```

### pandas.DataFrame.loc[] e .iloc[]

#### .loc[]

 .loc seleciona um grupo de linahs e colunas segundo os rótulos ou uma matriz booleana. Para selecionarmos um rótulo, simplesmente o passaremos entre colchetes. Nesse exemplo, selecionaremos o "Passat".

```python
dataset.loc["Passat"] 
'''
retorna toda uma  Series contendo dados referentes ao index "Passat" 
visto que definimos que o nome dos index (linhas) seria "Nome" referente ao nome dos carros.
'''
```

Podemos passar mais de um index para iloc para buscar mais de uma linha de nosso dataset, porém é necessário passar dentro de duplo colchetes para que o pandas entenda que buscamos outra linha e não uma linha e uma coluna.

```python
dataset[["Passat", "Jetta Variant"]]
'''
retorna toda um dataframe contendo os  dados referentes as linhas que possuem os rótulos "Passat" e "Jetta Variant" na sequência que foram chamadas dentro da função.
'''
```

agora se passarmos apenas : como primeiro parâmetro, receberemos todas as linhas do conjunto e somente as colunas selecionadas.

```python
dataset.loc[:, ['Motor', 'Valor']]
'''
retorna  um dataframe contendo os  dados referentes a todas as linhas e os valores das colunas "Motor" e "Valor".
'''
```

#### .iloc[] ou "index location"

O iloc também nos permite fazer seleções, mas se utiliza dos índices numéricos - ou seja, na posição das informações, sem se importar com rótulos. No primeiro exemplo, passaremos como parâmetro apenas 1, recebendo uma Series como retorno.

```python
dataset.iloc[1]
''' Retorno:

Motor Motor Diesel Ano 1991 Quilometragem 5712 Zero_km False Acessórios ['Central multimídia', 'Teto panorâmico', 'Fre... Valor 106162 
Name: Passat, dtype: object
'''
```

Se utilizarmos este mesmo comando porém com o duplo colchetes, receberemos este dado em formato de dataframe.

```python
dataset.iloc[[1]]
'''
Output:

Nome    Motor            Ano     Quilometragem   Zero_km     Acessórios	                                      Valor

Passat  Motor Diesel    1991     5712.0          False       ['Central multimídia', 'Teto panorâmico', 'Fre...   106161.94
'''
```

Para obtermos colunas específicas, passaremos, após uma vírgula, um novo par de colchetes contendo os índices das colunas que desejamos acessar. Não é necessário passá-los na mesma ordem do dataset original, algo que exemplificaremos na seleção abaixo, feita com as colunas 0, 5 e 2 ("Motor", "Valor" e "Quilometragem", respectivamente).

```python
dataset.iloc[[1:4], [0,5,2]]
'''Output:

Nome        Motor           Valor       Quilometragem

Passat      Motor Diesel    106161.94   5712.0
Crossfox    Motor Diesel V8 72832.16    37123.0
DS5         Motor 2.4 Turbo 124549.07   NaN
'''
#detalhe: é possível selecionar linhas também desordenadamente.
dataset.iloc[[1, 42, 22], [0, 5, 2]]

'''
Nome                    Motor                   Valor       Quilometragem
Jetta Variant           Motor 4.0 Turbo         88078.64    44410.0
Passat                  Motor Diesel            106161.94   5712.0
Crossfox                Motor Diesel V8         72832.16    37123.0
DS5                     Motor 2.4 Turbo	        124549.07   NaN
Aston Martin DB4        Motor 2.4 Turbo         92612.10    25757.0
... ... ... ...
Phantom 2013            Motor V8                51759.58    27505.0
Cadillac Ciel concept   Motor V8                51667.06    29981.0
Classe GLK              Motor 5.0 V8 Bi-Turbo   68934.03    52637.0
Aston Martin DB5        Motor Diesel            122110.90   7685.0
Macan                   Motor Diesel V6         90381.47    50188.0
'''
```


# Material de Consulta

## Links Úteis

[Python string.replace regular expression [duplicate]](https://stackoverflow.com/questions/16720541/python-string-replace-regular-expression)

[Python Docs - re — Operações com expressões regulares](https://docs.python.org/pt-br/3/library/re.html#module-contents)

[Replace strings in Python (replace, translate, re.sub, re.subn)](https://note.nkmk.me/en/python-str-replace-translate-re-sub/)

[Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/#metacharacters-supported-by-the-re-module)

[apply() - applying functions to list items](https://chrisalbon.com/python/basics/applying_functions_to_list_items/)

[Python Pandas .ix()](https://www.geeksforgeeks.org/python-pandas-dataframe-ix/)

[Multiindex columns Pandas](https://stackoverflow.com/questions/27420263/pandas-parse-merged-header-columns-from-excel)

[Hierarchical multindex - pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-hierarchical)

[cookbook multiindex - pandas ](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook-multi-index)

[Built-in functions python](https://docs.python.org/3.6/library/functions.html)

[XlsxWriter](https://xlsxwriter.readthedocs.io/index.html)

[Multiple Pandas dataframes to Excel](https://xlsxwriter.readthedocs.io/example_pandas_multiple.html#ex-pandas-multiple)

[]()


## [4.1 Python Built-in functions](https://docs.python.org/3.6/library/functions.html)
A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.

Utilizando a função pd.set_option() é possível definir alguns parâmetros do dataframe, como o número máximo de linhas retornadas, algo que configuraremos com display.max_rows seguido do número determinado de linhas, neste exemplo 1000.

```python
import pandas as pd
pd.set_option('display.max_rows', 1000)
```

Se executarmos dataset novamente, receberemos todas as 258 linhas - não foram mostradas 1000 pois nosso conjunto não possui esse total de informações. Também temos uma opção para exibir mais colunas, chamada display.max_columns. Como gostaríamos de manter a configuração padrão, comentaremos ambas as linhas.

```python
import pandas as pd
# pd.set_option('display.max_rows', 10000)
 #pd.set_option('display.max_columns', 1000)
```


## 5. PANDAS BÁSICO
versão: 0.25.2

Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.

## Estruturas de Dados
### Series
Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de index. A forma básica de criação de uma Series é a seguinte:

`````python
s = pd.Series(dados, index = index)
````

O argumento dados pode ser um dicionário, uma lista, um array Numpy ou uma constante.

### DataFrames
DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.

```python
    df = pd.DataFrame(dados, index = index, columns = columns)
```

O argumento dados pode ser um dicionário, uma lista, um array Numpy, uma Series e outro DataFrame.

[Documentação](https://pandas.pydata.org/pandas-docs/version/0.25/)


## A função zip()

Duas ferramentas bastante utilizadas quando iteramos com tuplas são o desempacotamento de tuplas e a built-in function zip().

Com o desempacotamento de tuplas, é possível fazer declarações conjuntas de variáveis e utilizar cada variável individualmente. Por exemplo:

```python
nome, valor = ('Passat', 100000.0)
```

A função zip() permite gerar um iterador de tuplas, como no exemplo abaixo:

````python
In [1]:
nomes = ['Passat', 'Crossfox']
valores = [100000.0, 75000.0]
list(zip(nomes, valores))

Out [1]:
[('Passat', 100000.0), ('Crossfox', 75000.0)]
```


## Operações básicas com dicionários

```python
dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
        }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
        }
    }
```

```python
 
nomes_carros = ['Jetta Variant', 'Passat', ('ecosport', 'ka', 'fiesta'), 'Polo']
nomes_carros = tuple(carros)
jetta, passat, ford, polo = nomes_carros
print(jetta, passat, ford, polo)

nomes_carros[2][1]

######################################################

nomes_carros = ['Jetta Variant', 'Passat', ('ecosport', 'ka', 'fiesta'), 'Polo']
nomes_carros = tuple(carros)

_, a, *_ = nomes_carros

print(a, _)


##############################################################
import re
marcas = ['porsche', 'lamborghini', 'audi', 'bmw', 'mercedes', 'jaguar']
modelos=['cayenne','murcielago','A6','325i','sl300','????']

a = zip(marcas,modelos)

for marca, modelo in zip(marcas, modelos): 
    if re.search('[rs]$', marca):
        print('marca: {} - modelo: {}'.format(marca, modelo))

#######################################################################
```

## formando dicts a partir de um iterador (.zip())
""" uma variavel que recebe um dict não copia os dados de um dict, simplesmente aponta para o mesmo endereço de memória, portanto para manipular um dict sem interferir no original é necessário usar o método dict.copy() : """

carros = dict((marca, modelo) for marca, modelo in zip (marcas, modelos))
outro_carros = carros
carros_copia = carros.copy()
modelo = carros.pop('jaguar')

'''o carros_copia que recebeu realmente uma cópia do dict não teve seu item "Jaguar"
apagado após o comando, mas o carros e outro_carros tiveram assim que o comando 
"carros.pop('jaguar') foi executado, o comando .pop(key, default) além de ter a possibilidade de tratamento de erro caso não seja encontrado a key passada pelo parametro "default" e a cada pop, o valor referenciado no item é retornado, portanto podemos salva-lo numa variável.'''

print(carros_copia, '\n', carros, '\n', outro_carros)

O método update() atualiza o dicionário e pode ser utilizado de duas formas:

```python

In [1]:
dados.update({'Passat': 85000, 'Fusca': 150000})

Out [1]:
{'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000, 'Passat': 85000, 'Fusca': 150000}

In [2]:
dados.update(Passat = 95000, Fusca = 160000)

Out [2]:
{'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000, 'Passat': 95000, 'Fusca': 160000}

```

Alternativa correta! Note que se a chave tiver um nome não válido para variáveis do Python (por exemplo: 'Jetta Variant'), o segundo formato não pode ser utilizado.

O método copy() cria uma cópia do dicionário
Alternativa correta! Funciona da mesma forma que aprendemos no curso anterior, quando falamos sobre as listas do Python.

## Métodos de dicionários:

Alguns exemplos:

```python
carros = dict((marca, modelo) for marca, modelo in zip (marcas, modelos))

carros.keys(), carros.values(), carros.items()

OUTPUT:

dict_keys(['porsche', 'lamborghini', 'audi', 'bmw', 'mercedes', 'jaguar']) 
dict_values(['cayenne', 'murcielago', 'A6', '325i', 'sl300', '????']) 
dict_items([('porsche', 'cayenne'), ('lamborghini', 'murcielago'), ('audi', 'A6'), ('bmw', '325i'), ('mercedes', 'sl300'), ('jaguar', '????')])
```


Utilize o dicionário abaixo para responder esta atividade:
```python
dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}
```
Selecione a alternativa que apresenta o código que imprime somente os nomes dos veículos com ano de fabricação maior ou igual a 2000.

```python
for item in dados.items():
    if(item[1]['ano'] >= 2000):
        print(item[0])
```
Alternativa correta! Veja que dados.items() retorna um iterador de tuplas, onde cada tupla tem como primeiro item a chave do dicionário e como segundo o respectivo valor:

In [1]:

```python
for item in dados.items():
    print(item)
```

```python
('Crossfox', {'valor': 72000, 'ano': 2005})
('DS5', {'valor': 125000, 'ano': 2015})
('Fusca', {'valor': 150000, 'ano': 1976})
('Jetta', {'valor': 88000, 'ano': 2010})
('Passat', {'valor': 106000, 'ano': 1998})
```

Para acessar a chave do dicionário, basta utilizar item[0], e para acessar o valor, basta usar item[1]. Para acessar o ano dentro do dicionário, usamos item[1]['ano'].

