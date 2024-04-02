from random import random

arr = list(range(1,45+1))

for i in range(100):
    rnd = int(random()*45)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp
    
# print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])

print(arr)

for i in range(5):
    print(arr.pop(i), end="  ")