class Jogo: 
    def __init__(self, nome: str, ano: int, console: str) -> object:
        self.nome = nome
        self.ano = ano
        self.console = console
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, value):
        if isinstance(value, str): 
            self._nome = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano (self, value):
        if not isinstance(value, int):
            raise KeyError('Váriavel ano deve ser um inteiro')
        self._ano = value 
    
    @property
    def console(self):
        return self._console

    @console.setter
    def console (self, value):
        if isinstance(value, str):
            self._console = value

mock_jogos = [  Jogo("Dark Souls II", 2014, "PS3,X360,PS4,XOne, Pc"),
                Jogo("Dark Souls III", 2016, "PS4,XOne, Pc"),
                Jogo("Monster Hunter World", 2018, "PS4,XOne, Pc"),
                Jogo("MegamanX", 1998, "Snes"), ]