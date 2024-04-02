from random import random

arr = [1,2,3]

for i in range(100):
    rnd = int(random()*3)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp
print(arr[0],arr[1])

