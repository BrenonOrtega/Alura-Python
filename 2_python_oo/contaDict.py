class Conta:
    def __init__ (self, titular, saldo=0, agencia="0000-0", limite = 1000):
        self._conta = {"titular": titular, "saldo": saldo, "agencia":agencia, "limite": limite}
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.limite = limite 
        

    def saque(self, quantia):
        self.saldo -= quantia
        return self.saldo

    def deposito(self, quantia):
        self.saldo += quantia
        return self.saldo

    def transferir (self, conta_destino, quantia):
        if (self.saldo >= quantia):
            self.saque(quantia)
            try:
                conta_destino.deposito(quantia)
            except:
                raise "A conta destino deve ser um objeto do tipo Conta."
        else:
            print("Você não possui saldo para transferir esta quantia!)
    
    def extrato (self):
        print (f"||Titular: {self.titular}||")
        print (f"||Saldo: R${self.saldo}  ||")
        print (f"||Agencia: {self.agencia}||")
        print (f"||Limite: R${self.limite}||")

    @property
    def titular(self):
        return self._conta["titular"]
    
    @property  
    def saldo(self):
        return self._conta["saldo"]

    @saldo.setter
    def saldo(self, novo_saldo):
        self._conta["saldo"] = novo_saldo
        self.saldo

    @property
    def agencia(self):
        return self._conta["agencia"]
    
    @agencia.setter
    def agencia(self, nova_agencia):
        self._conta["agencia"] = nova_agencia
        self.agencia
    
    @property
    def limite (self):
        return self._conta["limite"]
    
    @limite.setter
    def limite (self, novo_limite):
        self._conta["limite"] = novo_limite
        print(self.limite) 

    



        

