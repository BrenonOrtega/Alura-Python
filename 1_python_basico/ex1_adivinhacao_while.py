
msg = "Bem vindo ao jogo de adivinhacao!"
msg_espacamento = "**************************************"

print(msg_espacamento)
print (msg) 
print(msg_espacamento)

numero_secreto = 42
rodada = 1
maximo_tentativas = 5
fim_jogo = False

while not(fim_jogo):

    print("tentativa {} de {}.".format(rodada,  maximo_tentativas))

    if (rodada >= maximo_tentativas):
        fim_jogo = True

    chute_str = input("digite o seu chute:")
    chute_usuario = int(chute_str)

    chute_correto = (chute_usuario == numero_secreto)
    chute_menor   = (chute_usuario <  numero_secreto)
    chute_maior   = (chute_usuario >  numero_secreto)

    if chute_correto :
        msg = "Acertou!"
        fim_jogo = True

    else:
        rodada += 1

        if (chute_maior):
            msg = "Errow! Seu chute é maior que o número secreto!"

        elif (chute_menor):
            msg = "Errow! Seu chute é menor que o número secreto!"
        
    print(msg_espacamento)
    print ("Você chutou que o número correto é", chute_str)
    print (msg)
    print(msg_espacamento)

print ("fim do jogo!")
