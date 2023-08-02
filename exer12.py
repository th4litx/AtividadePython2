def calcular_mediana(lista):
    # Ordena a lista em ordem crescente
    lista_ordenada = sorted(lista)

    # Verifica se a lista tem um número ímpar de elementos
    if len(lista_ordenada) % 2 == 1:
        # Se for ímpar, a mediana é o elemento do meio
        mediana = lista_ordenada[len(lista_ordenada) // 2]
    else:
        # Se for par, a mediana é a média dos dois elementos do meio
        meio1 = lista_ordenada[len(lista_ordenada) // 2 - 1]
        meio2 = lista_ordenada[len(lista_ordenada) // 2]
        mediana = (meio1 + meio2) / 2

    return mediana

# Exemplo de uso da função
numeros = [10, 5, 20, 15, 8]
mediana_resultante = calcular_mediana(numeros)
print("Mediana dos números:", mediana_resultante)
