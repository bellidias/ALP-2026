def ola(name, genero):
    if genero == "feminino":
        return f"Olá, {name}, bem vinda!"
    elif genero == "masculino":
        return f"Olá, {name}, bem vindo!"
    else:
        return f"Olá, {name}, boas vindas!"
name = input("Qual é seu nome?")
genero = input("Qual é seu gênero? (feminino, masculino ou neutro)")
print(ola(name, genero))