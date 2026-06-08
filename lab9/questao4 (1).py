val1 = int(input("Digite o primeiro número: "))
val2 = int(input("Digite o segundo número: "))
if val1 > val2:
    print(f"O maior valor é: {val1}")
elif val2 > val1:
    print(f"O maior valor é: {val2}")
else:
    print("Ambos têm o mesmo valor.")