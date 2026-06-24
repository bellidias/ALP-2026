import random
import time
n = random.randint(2, 10)
time.sleep(n)
print("AGORA!!")
start = time.time()
input("Pressione ENTER rapidamente!!")
finish = time.time()
reacao = finish - start
print(f"Você levou {reacao:.4f} segundos para dar enter.")