cont = 5
while cont > 0:
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0:
        continue
    print(f'{num} é um número ímpar')
#O código pede para o usuário digitar apenas 5 números.
#Se o usuário não digitar um número ímpar,o código vai pedir de novo (apenas 5 vezes).
#Mas se ele digitar um número ímpar, ele imprimirá "tal número é ímpar"