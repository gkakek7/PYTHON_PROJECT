import requests
from bs4 import BeautifulSoup as bs
import datetime
from day04crawl.daostock import DaoStock
import time
ds=DaoStock()
res = requests.get("https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry")
now=datetime.datetime.now()
ymd=now.strftime("%Y%m%d_%H%M")

soup = bs(res.text,"html.parser")

names=soup.select(".st_name")

for idx,n in enumerate(names):
    s_name=n.text.strip()
    s_code=n.select("a")[0]['href'].split("/")[3]
    price=n.parent.select(".price")[0].text.replace(",","")
    cnt=ds.insert(s_name, price, s_code, ymd)
    print(idx,s_name,price,s_code,ymd)
    
    