soma = 0
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break 
    soma += i
    print(i, soma)