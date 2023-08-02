def calcular_media(lista):
    # Verifica se a lista não está vazia para evitar divisão por zero
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia

    # Calcula a soma de todos os números da lista
    soma = sum(lista)

    # Calcula a média dividindo a soma pelo número de elementos na lista
    media = soma / len(lista)

    return media

# Exemplo de uso da função
numeros = [10, 20, 30, 40, 50]
media_resultante = calcular_media(numeros)
print("A média dos números é:", media_resultante)
