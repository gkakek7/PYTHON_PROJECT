from day01.daonews import DaoNews
# 저장된 데이터 목록조회
dn=DaoNews();
list=dn.selectXYLabelList();
print(list)
# 데이터 저장
for i in list:
    dn.insertRecom(i[0], i[1], i[2], i[3])
    
