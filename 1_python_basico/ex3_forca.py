import random

def jogar():
    pula_linha = "\n"
    mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()
    segredo = inicializa_segredo(palavra_secreta)
    imprime_palavra_oculta(segredo)

    acertou = False
    enforcado = False   
    tentativas = 8
    while (not acertou and not enforcado):
        letra_digitada = pede_chute()
    
        if len(letra_digitada) == 1:  
            indice_letras = verifica_letra_digitada(letra_digitada, palavra_secreta)
        
            if len(indice_letras) > 0:
                for posicao_chute in indice_letras:
                    segredo[posicao_chute] = letra_digitada
                print(f"A letra {letra_digitada} existe na palavra secreta!", pula_linha)
            else:
                tentativas -= 1
                print (f"Você errou! {tentativas} tentativas restantes.", pula_linha)

            enforcado = tentativas == 0
            acertou = "_" not in segredo
            imprime_palavra_oculta(segredo)

        elif len(letra_digitada) == 0:
            print("É necessário digitar uma letra para jogar.")
        else:
            print("digite apenas uma única letra.")
        
    verifica_resultado(acertou, enforcado, palavra_secreta)

def mensagem_inicial():
    msg = "Bem vindo ao jogo de forca"
    msg_dica = "Neste jogo de forca, todas as palavras são pokemons lendários!"
    msg_espacamento = "**************************************"

    print(msg_espacamento)
    print(msg)
    print(msg_espacamento,"\n")

def carrega_palavra_secreta(arquivo="palavras.txt", linha_inicial=0):
    arquivo = open(arquivo, "r")
    palavras = []
    for line in arquivo:
        palavras.append(line.strip().upper())
    arquivo.close()

    numero = random.randrange(linha_inicial, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def verifica_letra_digitada(letra, palavra):
    index_letra = 0
    posicao_letras = []
    for i in palavra:
        if letra == i:
            posicao_letras.append(index_letra)
        index_letra += 1 
    return posicao_letras

def inicializa_segredo(palavra):
   return ["_" for letra in palavra]

def pede_chute():
    chute = input("digite uma letra:")
    chute = chute.strip().upper()
    return chute

def imprime_palavra_oculta(palavra_oculta):
    print('Palavra Secreta:'," ".join(map(str, palavra_oculta)))

def verifica_resultado(acerto, enforcou, palavra_secreta):
    if acerto:
        print("Você Acertou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    elif enforcou:
        print(f"Voce foi enforcado! x.x A palavra secreta era: \"{palavra_secreta.lower()}\"")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print('fim do jogo!')

if __name__ == "__main__":
    jogar()
