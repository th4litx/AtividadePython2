def fatorial(numero):
    # Verifica se o número é negativo, pois o fatorial não é definido para números negativos
    if numero < 0:
        return None

    # Inicializa o fatorial como 1
    fatorial_resultado = 1

    # Calcula o fatorial do número usando um loop for
    for i in range(1, numero + 1):
        fatorial_resultado *= i

    return fatorial_resultado

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
resultado = fatorial(numero)

if resultado is not None:
    print(f"O fatorial de {numero} é: {resultado}")
else:
    print("O fatorial não é definido para números negativos.")
