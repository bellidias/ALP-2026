n = int(input("Digite a quantidade de valores: "))
soma = 0
cont = 0
while cont < n:
    valor = int(input(f"Digite o {cont + 1}° número: "))
    soma += valor
    cont += 1
if n > 0:
    media = soma/n
    print("A soma dos números digitados é: ", soma)
    print("A quantidade de números digitados é: ", cont)
    print("A média é: ", media)
else:
    print("A quantidade n deve ser positiva.")