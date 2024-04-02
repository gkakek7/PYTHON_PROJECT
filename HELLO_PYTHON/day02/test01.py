# 1에서 10까지의 합을 구하시오
arr = range(1,10+1)
# print(list(arr))
sum = 0
for i in range(1,10+1):
    sum += i
print("sum =",sum)