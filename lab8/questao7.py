#que questão é essa, Camilaaa? Era mais fácil ir de elevador.
degrau = 1 
print("⋆.𐙚˚࿔ JOGO: Knockin' On Heaven's Door 𝜗𝜚⋆")
print("Objetivo:  Você está em uma escada, no degrau 1 e quer chegar ao degrau 100.")
while True:
    print(f"Degrau atual: {degrau}")
    if degrau >= 100:
        print("Parabéns! Você chegou à Heaven's Door.")
    passos = int(input("Digite o número de passos de 1 a 6 (ou 0 para desistir):"))
    if passos == 0 :
        print("Você desistiu.")
        break
    if passos < 1 or passos > 6:
        print("Valor inválido, tente novamente.")
        continue
    heavensdooor = degrau + passos
    print(f"Degrau: {heavensdooor}", end= "")
    if heavensdooor % 3 == 0:
        heavensdooor -= 1
        print("Multiplo de 3: Volte 1 degrau.")
    elif heavensdooor % 5 == 0:
        heavensdooor += 1
        print("Multiplo de 5: Avance mais 1 degrau.")
    elif heavensdooor % 7 == 1:
        heavensdooor += 4
        print("Multiplo de 7: Avance mais 4 degraus.")
    elif heavensdooor % 11 == 0:
        heavensdooor = 11
        print("Multiplo de 11: Volte para o início.")
    else:
        print()
    degrau = heavensdooor
        