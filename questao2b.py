soma = 0
while soma <= 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
#Erros: não adicionar uma variável que defina as 10 quantidades de números para digitar e somar.
#A variável "soma" serve apenas para somar os números digitados.
#corrigido:
soma = 0
cont = 0
while cont <= 9:
    num = int(input("Digite um número para somar:"))
    soma += num
    cont += 1
print("A soma dos 10 números é:", soma)
