#apenas adicionei o 'continue' na opção inválida.
tot = 0
while True:
    print("⋆.𐙚˚࿔ Cardápio 𝜗𝜚˚⋆")
    print("1. Cookie - R$4,50")
    print("2. Trufa - R$3,50")
    print("3. Cupcake - R$5,00")
    print("4. Fechar a conta")
    num = int(input("Digite o número da opção desejada"))
    if num == 1:
        tot += 4.50
        print("Cookie adicionado.")
    elif num == 2:
        tot += 3.50
        print("Trufa adicionada.")
    elif num == 3:
        tot += 5
        print("Cupcake adicionado.")
    elif num == 4:
        print(f"Valor da compra: R$ {tot:.2f}")
        break
    else:
        continue
    
