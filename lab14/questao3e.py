import random

def roleta():
    numero = random.randint(1, 36)
    
    if numero % 2 == 0:
        cor = "Preto"
    else:
        cor = "Vermelho"
    
    return numero, cor
num, cor = roleta()
print(f"{num}, {cor}")