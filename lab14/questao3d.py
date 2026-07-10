import time
def contagem_regressiva(n):
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)
n = int(input("Insira um valor:"))
contagem_regressiva(n)