class ProducaoCinematografica:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
 
    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Filme(ProducaoCinematografica):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"nome: {self.nome}, ano: {self.ano}, duração: {self.duracao}, likes: {self.likes}."


class Serie(ProducaoCinematografica):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'nome: {self.nome}, ano:{self.ano}, temporadas: {self.temporadas}, likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programacao):
        self.nome = nome
        self._programacao = programacao

    def __getitem__(self, item):
        return self._programacao[item]

    def __len__(self):
        return len (self._programacao)


vingadores = Filme("vingadores-guerra infinita", 2018, 160)
troia = Filme("troia", 2010, 120)

demolidor = Serie("demolidor da netflix", 2015, 3)
supernatural = Serie("supernatural", 2007, 9)

vingadores.nome = 'vingadores-guerra infinita parte 2'

vingadores.dar_like()
vingadores.dar_like()
troia.dar_like()
troia.dar_like()
supernatural.dar_like()
supernatural.dar_like()
demolidor.dar_like() 

filmes_series = [vingadores, demolidor, troia, supernatural]

minha_playlist = Playlist('fim de semana', filmes_series)

for programa in minha_playlist:
    print(programa)
 
'''corrigir len '''
print(f'len dessa lista é {len(minha_playlist)}')
