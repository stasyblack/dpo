import random
import time

def initListWithRandomNumbers():
    rand_list=[]
    n=1000
    for i in range(n):
        rand_list.append(random.randint(0, 999))
    return rand_list

def calcHist(tdata):
    hist=[0]*10
    for i in tdata:
        ind = i // 100
        if (ind > 9): ind = 9
            
        hist[ind] += 1

    return hist

a =  initListWithRandomNumbers()

max=-1
min=10
allTime=0
for i in range(100):
    start = time.time()
    calcHist(a)
    end = time.time()
    if (end-start<min):
        min=end-start
    if (end-start>max):
        max=end-start
    allTime=allTime+end-start
srTime=allTime/100
print("Maximum time is ", (max))
print("Minimum time is ", (min))
print ("Mean time is ", (srTime))