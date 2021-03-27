from prova import ordena_rank

def teste_cases():
    teste1 = [7]
    teste11 = [5, 10, 15, 20, 25, 30, 35, 40]
    teste12 = [10, 11, 16, 20]
    assert (ordena_rank(teste12, teste11)) == [10, 9, 7, 5, 4, 3, 2, 1]
    assert (ordena_rank(teste1, teste11)) == [9, 7, 6, 5, 4, 3, 2, 1]
    assert (ordena_rank(teste12, teste1)) == [5]