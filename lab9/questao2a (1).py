#4c, 10b, 7d, 12a, 3e
n = int(input("Digite um número: "))
if n % 2 == 0:
    if n > 10:
        print("A")
    elif n == 10:
        print("B")
    else:
        print("C")
elif n > 5:
    print("D")
else:
    print("E")