import random

def lancamento_dados():
    # Simula o lançamento de dois dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Calcula a soma dos valores obtidos nos dois dados
    soma = dado1 + dado2

    return soma

# Executa o lançamento dos dados e obtém a soma
resultado = lancamento_dados()
print("Resultado do lançamento dos dados:", resultado)
