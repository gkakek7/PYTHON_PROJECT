# 홀/짝을 선택하시오
# mine:홀
# com: 홀
# 결과: 승리
from random import random

mine = input("홀/짝을 선택하시오")

com = random()

print(com)

if com <= 0.5 :
    com = "짝"
else:
    com = "홀"
    
# 자바의 String에서만 equals 다른 모든 언어에서는 ==
if com == mine:
    result = "축하합니다! 컴퓨터를 상대로 승리하셨습니다!!!"
else:
    result = "이걸 지네...ㅉ"

print(f'사용자: {mine}')
print(f'컴퓨터: {com}')
print(result)
