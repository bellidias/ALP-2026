#A
#Código:
for i in range(1,5)
print(i * 2)
#Corrigido:
for i in range(1,5):
    print(i * 2)

#B
#Código:
soma = "0"
for num in range(10):
    soma = soma + num
print("Soma:", soma)
#Corrigido:
soma = 0
for num in range(10):
    soma = soma + num
print("Soma:", soma)

#C
#Código:
for num in range 3:
print f"O dobre de {num} é:"
    print num*2
#Corrigido:
for num in range(3):
    print(f"O dobro de {num*2} é:")

#D
#Código:
numero = random.randint(1,10)
for i in range(3):
    n = input('Adivinhe o número:')
    if n == numero:
        print('Correto')
        break
#Corrigido:
import random
numero = random.randint(1,10)
for i in range(3):
    n = int(input('Adivinhe o número:'))
    if n == numero:
        print('Correto')
        break
    else:
        print('Errou')
else:
    print(f'Acabaram suas chances. O número era {numero}')