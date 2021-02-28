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
