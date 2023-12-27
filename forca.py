import random


def jogar():
    print_mensagem_abertura()

    palavra_secreta = seleciona_palavra_secreta()

    letras_certas = inicializa_letras_certas(palavra_secreta)
    print(" ".join(letras_certas))

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:
        chute = input_chute()

        if len(chute) > 1:
            print("Digite apenas uma letra!")

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_certas, palavra_secreta)

        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_certas
        print(" ".join(letras_certas))

    if acertou:
        print_mensagem_ganhador()
    else:
        print_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def print_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def seleciona_palavra_secreta(nome_arquivo="palavras.txt"):
    with open(nome_arquivo, "r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    return palavra_secreta


def inicializa_letras_certas(palavra):
    return ["_" for letra in palavra]


def input_chute():
    chute = input("Qual letra?")
    return chute.strip().lower()


def marca_chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra.lower():
            letras_certas[index] = letra
        index += 1


def print_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


def print_mensagem_ganhador():
    print("Parabéns, você ganhou!")
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


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
