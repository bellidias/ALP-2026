N = int(input("Digite a quantidade de jogos do galo: "))
vitorias = 0
empates = 0
derrotas = 0
for i in range(N):
    galo = int(input("Digite a quantidade de gols do Galo: "))
    oponente = int(input("Digite a quantidade de gols do Oponente: "))
    if galo > oponente:
        vitorias += 1
    elif galo < oponente:
        derrotas += 1
    elif galo == oponente:
        empates += 1
pontuacao = (vitorias * 3) + (derrotas * 0) + (empates * 1)
print(f'Vitórias: {vitorias}')
print(f'Empates: {empates}')
print(f'Derrotas: {derrotas}')
print(f'Pontuaçaõ: {pontuacao}')