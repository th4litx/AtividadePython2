def calcular_soma():
    # Inicialize a variável que armazenará a soma
    soma = 0

    # Use um loop for para percorrer os números de 1 a 100
    for num in range(1, 101):
        # Adicione o número atual à soma
        soma += num

    # Retorne o resultado da soma
    return soma

# Chame a função e imprima o resultado
resultado = calcular_soma()
print("A soma dos números de 1 a 100 é:", resultado)
