def contar_ocorrencias_palavras(texto):
    # Cria um dicionário para armazenar as palavras e suas contagens
    contagem_palavras = {}

    # Separa o texto em palavras (ignorando pontuação e espaços em branco)
    palavras = texto.lower().split()

    # Percorre todas as palavras do texto
    for palavra in palavras:
        # Remove qualquer pontuação ao redor da palavra
        palavra = palavra.strip(",.!?():;\"'")

        # Atualiza o contador da palavra no dicionário
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    return contagem_palavras

# Exemplo de uso da função
texto = input("Digite um texto: ")
ocorrencias_palavras = contar_ocorrencias_palavras(texto)

# Exibe as ocorrências de cada palavra
print("Ocorrências de cada palavra:")
for palavra, ocorrencias in ocorrencias_palavras.items():
    print(f"{palavra}: {ocorrencias}")
