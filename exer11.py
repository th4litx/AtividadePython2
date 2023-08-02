import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    tentativas = 0
    while True:
        # Solicita ao jogador para fazer um palpite
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        # Verifica se o palpite é igual ao número secreto
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente novamente! O número é maior.")
        else:
            print("Tente novamente! O número é menor.")

# Chama a função para iniciar o jogo de adivinhação
jogo_adivinhacao()
