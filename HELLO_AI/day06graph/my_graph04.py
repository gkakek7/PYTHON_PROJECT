import matplotlib.pyplot as plt
from day06graph.daostock import DaoStock
import numpy as np
de=DaoStock()

prices=[]
prices.append(de.selectArr("LG"))
prices.append(de.selectArr("삼성전자"))
prices.append(de.selectArr("마니커"))
prices.append(de.selectArr("서울식품"))

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

xs=np.ones((4),dtype=np.int8)
print(xs)

ax.plot(xs*0, [0, 1, 2, 3], prices[0], 'r')
ax.plot(xs*1, [0, 1, 2, 3], prices[1], 'g')
ax.plot(xs*2, [0, 1, 2, 3], prices[2], 'b')
ax.plot(xs*3, [0, 1, 2, 3], prices[3], 'y')

plt.show()