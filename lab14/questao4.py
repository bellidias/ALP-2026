#essa questão eu pesquisei para entender.
def soma_digitos(n):
    soma = 0
    while n > 0:
        soma += n % 10
        n = n // 10
    return soma
num = int(input("Digite um número inteiro: "))
resultado = soma_digitos(abs(num))
print(f"A soma dos digitos é: {resultado}")