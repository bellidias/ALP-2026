maior = float('inf')
while soma <= 10:
    num = int(input("Digite um número:"))
    if num > maior:
        maior = num
print('O maior número é:', maior)
#Erro1: para encontrar o maior, deve-se começar com o menor valor possível, ou seja, float('-inf')
#Erro2: é necessário um contador para ler os números.
#Erro3: a variável 'soma' não foi definida.

#corrigido:
maior = float('-inf')
cont = 1
while cont <= 10:
    num = int(input("Digite um número:"))
    if num > maior:
        maior = num
    cont += 1
print('O maior número é:', maior)