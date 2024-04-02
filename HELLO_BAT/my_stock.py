import requests
import time
import datetime
from daostock import DaoStock
from bs4 import BeautifulSoup as bs
ds=DaoStock()
now=datetime.datetime.now()
ymd=now.strftime("%Y%m%d_%H%M")

res = requests.get("https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry")
soup = bs(res.text,"html.parser")

names=soup.select(".st_name")

for idx,n in enumerate(names):
    s_name=n.text.strip()
    s_code=n.select("a")[0]['href'].split("/")[3]
    price=n.parent.select(".price")[0].text.replace(",","")
    cnt=ds.insert(s_name, price, s_code, ymd)
    print(idx,s_name,price,s_code,ymd)
    
    