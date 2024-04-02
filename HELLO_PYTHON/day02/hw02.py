# 업앤다운
from random import random

com = int(random()*99)
##print(com)

count =1
for i in range(1+10):
    mine = input("숫자를 입력하시오")

    mmine = int(mine)
    ##print(com)
    if mmine > com :
        print(f'{mmine}보다 down!')
        count += 1
    elif mmine < com:
        print(f'{mmine}보다 UPUPUP"')
        count += 1
    elif mmine == com:
        print("정답입니다!")
        print(f'{count}번 도전했따')
        break
    
print("10번의 기회를 모두 소진했습니다...ㅋ")