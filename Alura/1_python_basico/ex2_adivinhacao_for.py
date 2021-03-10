import random

def jogar():
    msg = "Bem vindo ao jogo de adivinhacao!"
    msg_instrucoes = "Neste jogo você deve adivinha qual é o número secreto!\nO numero muda a cada tentativa incorreta."
    msg_espacamento = "********************************************************"

    print(msg_espacamento)
    print(msg)
    print(msg_instrucoes)
    print(msg_espacamento)
    print("Selecione o nível de dificuldade:")
    dificuldade = int(input ("(1) Fácil | (2) Médio| (3) Dificil\n"))

    if dificuldade == 1:
        maximo_tentativas = 20

    elif dificuldade == 2:
        maximo_tentativas = 10

    elif dificuldade == 3:
        maximo_tentativas = 5

    else:
        print ("Dificuldade inválida!")
        quit()

    rodada = 1
    numero_maximo = 30
    pontos = 1000

    #Inicio do jogo
    print(msg_espacamento)
    print (msg) 
    print(msg_espacamento)

    for rodada in range(1, maximo_tentativas + 1):

        print("tentativa {} de {}.".format(rodada,  maximo_tentativas))
        
        numero_secreto = random.randrange(1, numero_maximo)
        numero_digitado = False

        while not numero_digitado:
            chute_str = input("digite o seu chute:")

            try:
                chute_usuario = int(chute_str)
                numero_digitado = True

                chute_correto = (chute_usuario == numero_secreto)
                chute_menor   = (chute_usuario <  numero_secreto)
                chute_maior   = (chute_usuario >  numero_secreto)
                

                if (chute_usuario < 1 or chute_usuario > numero_maximo):
                    print("Digite um número entre 1 e {}!".format(numero_maximo))
                    print(msg_espacamento)
                    continue

                else:
                    print(msg_espacamento)
                    print ("Você chutou que o número correto é", chute_str)

                    if chute_correto :
                        msg = "Você acertou o número e está com {} pontos!".format(pontos)
                        print (msg)
                        break

                    else:
                        rodada += 1

                        pontos_perdidos = abs(numero_secreto - chute_usuario)
                        pontos -= pontos_perdidos

                        print (f"O número correto era {numero_secreto}")
                        print (f"Você agora possui {pontos} pontos.")

                        if (chute_maior):
                            msg = "Errow! Seu chute é maior que o número secreto!"

                        elif (chute_menor):
                            msg = "Errow! Seu chute é menor que o número secreto!"
                            
            except:
                print("Por Favor digite um número!")
            
        print(msg_espacamento)

    print ("fim do jogo!")

if __name__ == "__main__":
    jogar()

