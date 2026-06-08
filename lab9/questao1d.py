soma = 0
cont = 1
x = int(input("Digite um valor: "))
while cont <= x:
    if cont % 2 != 0:
        soma += x
    cont += 1
print("A soma dos valores pare digitados é:", soma)