soma = 0
i = 0
while i < 10:
    print(i, soma)
    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    soma += i