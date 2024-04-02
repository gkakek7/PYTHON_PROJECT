import requests
import time
from bs4 import BeautifulSoup as bs
from _datetime import datetime
from day04crawl.daostock import DaoStock

res = requests.get("https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry")

# print(res.text)
soup = bs(res.text, "html.parser")
stocks=soup.select(".st_name")
cnt=0;
while True:
    for idx,i in enumerate(stocks):
        stock_item=i.parent
        stock_price=stock_item.select_one('.price')
        stock_code=stock_item.select_one('a')
        stock_name=stock_item.select_one('.name')
        s_name=""
        s_price=""
        s_code=""
        ymd=""
        if stock_name:
            s_name=stock_name.text
            
        if stock_price:
            price_n=stock_price.text
            price=price_n.replace(",","")
        if stock_code:
            href_value = stock_code['href']
            href=href_value.split('/')
            s_code=href[-1]
    
            
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M")
        ymd=current_datetime
        
        
        de=DaoStock()
        cnt+=de.insert(s_name, price, s_code, ymd)
    
    print(str(cnt)+"개 적용 완료")
    time.sleep(60)
    