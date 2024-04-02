import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from day01.daonews import DaoNews
driver = webdriver.Firefox()
dn=DaoNews()
list=dn.selectNewsCgList()
for idx, i in enumerate(list):
    driver.get(i[1])
    title=driver.find_element(By.CSS_SELECTOR,".media_end_head_title span")
    title=title.text.replace('”', "")
    title=title.replace('"', "")
    title=title.replace('“', "")
    img=driver.find_element(By.CSS_SELECTOR,"#img1")
    src=img.get_attribute("src")
    div=driver.find_element(By.CSS_SELECTOR,".ct_scroll_wrapper")
    repot=driver.find_element(By.CSS_SELECTOR, ".media_end_head_journalist_name").text;
    date_reg=driver.find_element(By.CSS_SELECTOR, ".media_end_head_info_datestamp_time").text;
    
    cnt=dn.updateNewsCg(i[0],title,src,date_reg,repot);
driver.get(list[0][1])

# print(src)
