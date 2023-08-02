def imprimir_numeros_naturais(n):
    # Verifica se o número informado é positivo
    if n < 0:
        print("Por favor, informe um número inteiro positivo.")
        return

    # Imprime os números naturais de 0 até N (inclusive)
    for i in range(n + 1):
        print(i)

# Solicita ao usuário para informar um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Chama a função para imprimir os números naturais de 0 até N
print("Números naturais de 0 até", numero, "em ordem crescente:")
imprimir_numeros_naturais(numero)
