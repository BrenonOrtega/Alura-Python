class Conta:
    def __init__ (self, titular, saldo=0, agencia="0000-0", limite = 1000):
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite         

    def saque(self, quantia):
        if (self.__aprova_saque(quantia)):
            self.saldo -= quantia
        else:
            print(f"O valor {quantia} ultrapassa o limite da conta.\nVocê não pode sacar essa quantia!")

    def deposito(self, quantia):
        self.saldo += quantia
        return self.saldo

    def transferir (self, conta_destino, quantia):
        self.saque(quantia)
        try:
            conta_destino.deposito(quantia)
        except:
            raise "A conta destino deve ser um objeto do tipo Conta."
    
    def extrato (self):
        print (f"||Titular: {self.titular}||")
        print (f"||Saldo: R${self.saldo}  ||")
        print (f"||Agencia: {self.agencia}||")
        print (f"||Limite: R${self.limite}||")

    def __aprova_saque(self, valor_saque):
        valor_maximo_saque = self.saldo + self.limite
        return valor_saque <=valor_maximo_saque
            

    @property
    def titular(self):
        return self.__titular
    
    @property  
    def saldo(self):
        return self.__saldo

    @saldo.setter    
    def saldo(self, quantia):
        self.__saldo = quantia
        

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, nova_agencia):
        self.__agencia = nova_agencia
        self.agencia
    
    @property
    def limite (self):
        return self.__limite
    
    @limite.setter
    def limite (self, novo_limite):
        self.__limite
        print(self.limite) 

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "caixa":"104", "Bradesco":"237"}

    



        

