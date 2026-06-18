import random

pt_p1 = 0
pt_p2 = 0
rodada = 1

while pt_p1 < 50 and pt_p2 < 50:
    print(f"======= RODADA {rodada} =======")
    
    p1 = int(input(f"Jogador 1 ({pt_p1} pontos): Qual o seu palpite para a soma?"))
    p2 = int(input(f"Jogador 2 ({pt_p2} pontos): Qual o seu palpite para a soma?"))
    print(f"🎲 Rolando os dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    result = dado1 + dado2
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Resultado: {result}")
    
    #distancia
    dist1 = abs(p1 - result)
    dist2 = abs(p2 - result)
    
    if dist1 < dist2:
        pt_p1 += 5
        print("Jogador 1 ganhou 5 pontos!")
    elif dist2 < dist1:
        pt_p2 += 5
        print("Jogador 2 ganhou 5 pontos!")
    else:
        pt_p1 += 2
        pt_p2 += 2
        print("⚖️ Empate! Ambos ganham 2 pontos!")
    rodada += 1
    print()
    
print("======= FIM DE JOGO =======")
if pt_p1 >= 50:
    print(f"🏆 O vencedor foi o jogador 1, com {pt_p1} pontos!")
else:
    print(f"🏆 O vencedor foi o jogador 2, com {pt_p2} pontos!")