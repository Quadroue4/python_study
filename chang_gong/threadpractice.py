import random
import threading
import time

def getNum():
    time.sleep(1)
    a = random.randint(1, 5)
    print(a)


while True:
    t = threading.Thread(target=getNum)
    t.start()
    print('-')