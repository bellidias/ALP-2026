#usei as condições que não se aplicam às cédulas.
while True:
    valor = int(input('Digite o valor que deseja sacar:'))
    if valor == 10 or valor == 30 or valor %10 != 0 or valor == 0:
        print("Valor inválido. Tente outro.")
        continue
    print("Saque realizado!")
    break