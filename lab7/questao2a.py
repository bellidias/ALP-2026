#O problema do código é ele não parar de solicitar ao usuário que ele digite um número. Isso acontece pelo script não possuir o contador na função while e no último print
N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0
while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
print(f"Quantidade de ímpares: {impares}")

#corrigido:
N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    contador += 1
        
print(f"Quantidade de ímpares entre 1 e {contador}: {impares}")
