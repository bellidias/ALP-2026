import random
import time 
n = random.randint(0, 10)
for i in range(1, n+1):
    print(f"volta {i}: Mais uma volta!")
    time.sleep(1)