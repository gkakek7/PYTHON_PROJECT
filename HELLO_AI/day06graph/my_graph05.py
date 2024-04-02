import matplotlib.pyplot as plt
from day06graph.daostock import DaoStock
import numpy as np
de=DaoStock()

s_names=["삼성전자","서울식품"]
prices=[]
for i in s_names:
    prices.append(de.selectArrN(i))

cnt_t=len(prices[0])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

xs=np.ones((cnt_t),dtype=np.int8)

print(xs)
for idx, i in enumerate(s_names):
    tp=(prices[idx]/prices[idx][0])*100
    ax.plot(xs*idx, list(range(cnt_t)), tp, '')

plt.show()