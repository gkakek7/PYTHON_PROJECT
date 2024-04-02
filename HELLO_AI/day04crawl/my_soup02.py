import requests
from bs4 import BeautifulSoup as bs

res = requests.get("http://localhost:8888/HELLO_WEB_EMP/emp_list")

# print(res.text)
soup = bs(res.text, "html.parser")
trs=soup.select("tr")

for idx,t in enumerate(trs):
    if idx==0:
        continue
    tds=t.select("td")
    print(tds[1].text,tds[3].text)
