import random # essa deve ser a primeira linha do código

num = random.randint(1, 10)
chances = 5
while chances > 0:
    chute =int(input("Escolha um número de 1 a 10 (5 chances):"))
    chances -= 1
    if chute == num:
        print("Parabéns, você acertou o número sorteado!")
        break
    elif chances == 0:
        print(f"Você gastou todas as suas chances. O número sorteado era {num}.")