import random
import time

karakter = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    print("".join(random.choice(karakter) for _ in range(50)))
    time.sleep(0.1)
