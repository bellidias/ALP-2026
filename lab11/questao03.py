while True:
    import time
    import random
    prob = random.randint(1, 10)
    if prob <=5:
        resposta='SIM'
    else:
        resposta='NÃO'
    yon = input("Deseja fazer uma pergunta?")
    if yon == "N" or yon == "n" or yon == "não" or yon == "NÃO":
        print("Tudo bem!")
        break
    if yon == "s" or yon == "S" or yon == "sim" or yon == "SIM":
        read = input("Qual é a pergunta?")
        print("Um segundo...")
        time.sleep(2)
        print("Quase lá...")
        time.sleep(2)
        print("Pensando na resposta...")
        time.sleep(2)
        print("JÁ SEI!")
        print(resposta)