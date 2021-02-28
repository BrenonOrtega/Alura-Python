from conta import Conta

conta = Conta("Brenon", 1200, "1234-5", 40000)

conta.extrato()

print ("\n")

conta.limite = 12
conta.deposito(250.0) 

conta.extrato()

conta.titular = "bryan"
