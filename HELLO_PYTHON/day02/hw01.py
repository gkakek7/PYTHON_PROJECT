# 가위/바위/보를 선택하시오
# mine:가위
# com: 보
# 결과: 이김
from random import random

mine = input("가위/바위/보를 선택하시오")
print("1=가위 2=바위 3=보")
com = int(random()*3+1)

print("컴퓨터",com)

if mine == "가위" :
    mine = 1
elif mine == "바위":
    mine = 2
elif mine == "보":
    mine = 3

print("사용자",mine)

if mine-com == 2 or mine-com == -1:
    print("패배")
elif mine-com == 1 or mine-com == -2:
    print("승리")
else :
    print("무승부")