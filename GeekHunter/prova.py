#Exercicio feito no hackertest da geek hunter

""" Em uma firma os vendedores possuem um rank que é ordenado pelo número de vendas, 
Não existe critério de desempate portanto se o primeiro lugar tiver 2 valores identicos,
os dois são primeiros lugares, carlos gostaria de fazer simulações no caso de vender
um x quantidade de valores (por exemplo 20, 10 e 35 vendas) em qual posição ele ficaria
em cada uma delas. crie uma função que retorne ao carlos a posição que ele ficaria com cada
uma das quantidades de vendas em sua simulação."""
""" Vendas do Evento """
V=[30, 12, 30, 18, 12]
""" Simulação do Carlos"""
C=[20, 10, 35]

"""Test cases da prova """
teste1 = [7]
teste11 = [55, 100, 100, 40, 100, 50, 35, 3]
teste12 = [20, 60, 40, 10]

def ordena_rank(lista_rank, lista_comparativa):
    lista_sem_repeticoes = set(lista_rank + lista_comparativa)
    lista_ordenada = sorted(list(lista_sem_repeticoes), reverse=True)
    tamanho_lista_ordenada = range(len(lista_ordenada))
    lista_comparativa_ordenada = zip(range(len(lista_comparativa)), lista_comparativa)

    resultado = []
    for dado in lista_comparativa:
        indice_valor = zip(tamanho_lista_ordenada, lista_ordenada)
        for  indice, valor in indice_valor:
            if dado == valor:
                posicao_valor = indice + 1
                resultado.append(posicao_valor)
    return resultado
