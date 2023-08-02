def ordenar_lista_crescente(lista):
    # Utiliza o método sort() para ordenar a lista em ordem crescente
    lista.sort()
    return lista

# Exemplo de uso da função
numeros = [10, 5, 20, 15, 8, 99,123]
numeros_ordenados = ordenar_lista_crescente(numeros)
print("Lista ordenada:", numeros_ordenados)
