import random
import time

def initRandom(size):
    rand=[]
    for i in range(size):
        rand.append(random.randint(0, 999))
    return rand

def calcHist():
    

random.seed(time.time())
n=100
arr_size = int(1e6)
a = []
a = initRandom(arr_size)
for i in range(n):
    start = time.time()
    a = calcHist()
    end = time.time()