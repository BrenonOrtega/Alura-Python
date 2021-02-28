import ex2_adivinhacao_for
import ex3_forca

def escolhe_jogo():
    msg = "Escolha seu jogo!"
    msg_espacamento = "**************************************"

    print(msg_espacamento)
    print(msg)
    print(msg_espacamento,"\n")

    msg = "(1) Forca | (2) Adivinhação"
    print(msg)

    jogo = int(input("Digite o comando do jogo desejado: "))

    if jogo == 1:
        print("jogando forca!")
        ex3_forca.jogar()

    elif jogo == 2:
        print ("Jogando adivinhação!")
        ex2_adivinhacao_for.jogar()

if __name__ == "__main__":
    escolhe_jogo()