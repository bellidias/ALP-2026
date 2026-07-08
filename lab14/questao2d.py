def calc(num1, num2, op):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    if op == "/":
        result = num1 / num2
    return result
num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
op = input("Qual é o operador?")
print(calc(num1, num2, op))