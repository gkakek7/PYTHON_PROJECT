from random import random

def getHollJJak():
    com = random()
    print(com)
    if com<= 0.5:
        com = "홀"
    else:
        com = "짝"
    return com

com = getHollJJak()
print("com",com)