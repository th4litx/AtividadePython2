def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None

    # Inicializa a maior e a menor palavra com a primeira palavra da lista
    maior_palavra = lista_palavras[0]
    menor_palavra = lista_palavras[0]

    # Percorre a lista para encontrar a maior e a menor palavra
    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra

# Exemplo de uso da função
lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
maior, menor = encontrar_maior_menor_palavra(lista_palavras)

if maior and menor:
    print("Maior palavra:", maior)
    print("Menor palavra:", menor)
else:
    print("A lista de palavras está vazia.")
