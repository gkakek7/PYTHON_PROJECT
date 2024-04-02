# 출력할 단수를 입력하세요 2
# 2*1=2 ...(밑으로)

a = input("출력할 단수를 입력하세요")
# aa = int(a)
# print(a+"*"+str(1)+"="+str(1*aa))

for i in range(1,9+1):
    c = int(a) * i
    print("{}*{}={}".format(a,i,c))