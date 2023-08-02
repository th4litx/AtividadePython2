def verificar_palindromo(palavra):
    # Remover espaços em branco e transformar tudo em minúsculas para ignorar maiúsculas e minúsculas
    palavra = palavra.replace(" ", "").lower()

    # Verificar se a palavra é igual à sua forma invertida
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Exemplo de uso da função
palavra_exemplo = "Reviver"
resultado = verificar_palindromo(palavra_exemplo)

if resultado:
    print(f'A palavra "{palavra_exemplo}" é um palíndromo!')
else:
    print(f'A palavra "{palavra_exemplo}" não é um palíndromo.')
