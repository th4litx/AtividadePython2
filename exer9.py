def palavras_maiusculas(lista_strings):
    # Cria uma lista vazia para armazenar as palavras em letras maiúsculas
    palavras_maiusculas_lista = []

    # Percorre a lista de strings
    for palavra in lista_strings:
        # Adiciona a palavra em letras maiúsculas à lista
        palavras_maiusculas_lista.append(palavra.upper())

    return palavras_maiusculas_lista

# Exemplo de uso da função
lista_strings = ["thalita", "python", "programação", "exemplo", "lista"]
resultado = palavras_maiusculas(lista_strings)
print("Palavras em letras maiúsculas:", resultado)
