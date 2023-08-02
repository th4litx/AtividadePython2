def encontrar_maior_menor_numero():
    # Solicita ao usuário para informar os números separados por espaço
    numeros_str = input("Digite uma sequência de números separados por espaço: ")

    # Converte os números em uma lista de inteiros
    numeros = [int(num) for num in numeros_str.split()]

    # Verifica se a lista não está vazia
    if not numeros:
        return None, None

    # Inicializa o maior e o menor número com o primeiro número da lista
    maior_numero = numeros[0]
    menor_numero = numeros[0]

    # Percorre a lista para encontrar o maior e o menor número
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

# Chama a função para encontrar o maior e o menor número da sequência
maior, menor = encontrar_maior_menor_numero()

if maior and menor:
    print("Maior número:", maior)
    print("Menor número:", menor)
else:
    print("A sequência de números está vazia.")
