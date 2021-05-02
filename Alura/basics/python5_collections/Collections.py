class ContaCorrente:
    __codigos= []
    def __init__(self, codigo):
        if codigo not in ContaCorrente.__codigos:
            self.codigo = codigo 
            ContaCorrente.__codigos.append(self.codigo)
            self._saldo = 0
        else:
            raise NameError("Conta já existe.")

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def deposita(self, value):
        self._saldo += value
        return self.saldo

    def __str__(self):
        return f"Conta código {self.codigo} - Saldo R${self.saldo}"


contas = []
contas.append( ContaCorrente(1) )
contas.append( ContaCorrente(2) )
contas.append( ContaCorrente(3) )
contas.append( ContaCorrente(4) )

for conta in contas:
    print(conta)