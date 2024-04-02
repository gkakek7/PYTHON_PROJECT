import matplotlib.pyplot as plt
from day06graph.daostock import DaoStock
from datetime import datetime

de=DaoStock()
samsung=de.selectList("삼성전자")
sk=de.select("SK")
lg=de.select("LG")
hanhwa=de.select("한화시스템")
posco=de.select("포스코스틸리온")
samPriceList = []
skPriceList = []
lgPriceList = []
hanhwaPriceList = []
poscoPriceList = []

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for idx, i in enumerate(samsung):
    if idx!=0 :
        firstPrice = samsung[idx-1].get('price')
        price = i.get('price')
        gap = price - firstPrice
        percent = gap/firstPrice*100
        samPriceList.append(percent)
        x1.append(0)
        y1.append(idx)
    
for idx, i in enumerate(sk):
    if idx!=0 :
        firstPrice = sk[idx-1].get('price')
        price = i.get('price')
        gap = price - firstPrice
        percent = gap/firstPrice*100
        skPriceList.append(percent)
        x2.append(1)
        y2.append(idx)
    
for idx, i in enumerate(lg):
    if idx!=0 :
        firstPrice = lg[idx-1].get('price')
        price = i.get('price')
        gap = price - firstPrice
        percent = gap/firstPrice*100
        lgPriceList.append(percent)
        x3.append(2)
        y3.append(idx)
    
for idx, i in enumerate(hanhwa):
    if idx!=0 :
        firstPrice = hanhwa[idx-1].get('price')
        price = i.get('price')
        gap = price - firstPrice
        percent = gap/firstPrice*100
        hanhwaPriceList.append(percent)
        x4.append(3)
        y4.append(idx)
    
for idx, i in enumerate(posco):
    if idx!=0 :
        firstPrice = posco[idx-1].get('price')
        price = i.get('price')
        gap = price - firstPrice
        percent = gap/firstPrice*100
        poscoPriceList.append(percent)
        x5.append(4)
        y5.append(idx)
    
    
fig=plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')  
ax.plot(x1, y1, samPriceList, 'r')
ax.plot(x2, y2, skPriceList, 'g')
ax.plot(x3, y3, lgPriceList, 'b')
ax.plot(x4, y4, hanhwaPriceList, '')
ax.plot(x5, y5, poscoPriceList, '')

plt.show()  