def numeros_pares(lista):
    # Cria uma lista vazia para armazenar os números pares
    numeros_pares_lista = []

    # Percorre a lista de números
    for num in lista:
        # Verifica se o número é par
        if num % 2 == 0:
            # Se for par, adiciona o número à lista de números pares
            numeros_pares_lista.append(num)

    return numeros_pares_lista

# Exemplo de uso da função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
numeros_pares_resultantes = numeros_pares(numeros)
print("Números pares:", numeros_pares_resultantes)
