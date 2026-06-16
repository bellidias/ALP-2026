while True:
    piada = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N")
    if piada == "s" or piada == "S" or piada == "sim" or piada == "SIM":
        continue
    if piada == "n" or piada == "N" or piada == "não" or piada == "NÂO":
        print("Obrigada. Tenha um bom dia! ;)")
        break
    else:
        print(f"{piada} Não é uma resposta válida de sim ou não.")