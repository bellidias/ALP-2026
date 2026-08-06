def conversao(n):
    f = (n * 1.8)+32
    return f 
n = int(input("Digite uma temperatura (celsius):"))
print(f"A conversão de {n} para fahrenheit é {conversao(n)}")