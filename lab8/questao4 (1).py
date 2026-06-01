soma = 0
while True:
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        continue
    if numero == 0:
        break
    soma += numero
    if soma > 100:
        break
print(f"A soma total é: {soma}")