from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, FirefoxOptions
str = "가나다라마바사아자차";
arr_three=[]
for i in range(10):
    mychar=str[i:i+1]
    for j in range(16):
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0,   'ry':0})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0,   'ry':0.5})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0,   'ry':-0.5})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0.5, 'ry':0})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0.5, 'ry':0.5})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':0.5, 'ry':-0.5})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':-0.5,'ry':0})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':-0.5,'ry':0.5})
        arr_three.append({'i':'{}{}'.format(mychar,j),  'rx':-0.5,'ry':0.5})
        
print(arr_three)
opts = FirefoxOptions()
opts.add_argument("--width=600")
opts.add_argument("--height=600")

driver = Firefox(options=opts)
cnt=0;
for i in arr_three:
    driver.get("http://127.0.0.1:5000/static/examples/_ex99?i={}&rx={}&ry={}".format(i['i'],i['rx'],i['ry']))
    # driver.save_screenshot("임시.png")
    obj_span = driver.find_element(By.TAG_NAME, 'canvas')  
    if cnt==10:
        cnt=0
    time.sleep(0.5)
    driver.save_screenshot(f"{i['i']}_{cnt}.png")
    cnt+=1