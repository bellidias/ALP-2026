import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite < 1 and palpite > 10:
        continue
    elif palpite != secreto:
        chances -= 1
        print("Errou,tente de novo!")
    elif palpite == secreto:
        print("Acertouu!")
        break
if chances == 0:
    print("Suas chances acabaram.")