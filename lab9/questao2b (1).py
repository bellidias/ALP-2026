#2:s3p3 3:s6p9 4:s10p9 10:s10p9break
soma = 0
produto = 3
valor = int(input("Digite um valor: "))
cont = 1
while(cont <= valor):
    if soma > produto:
        break
    soma += cont
    if cont % 2 != 0:
        produto *= cont
    cont += 1
print(soma, produto)