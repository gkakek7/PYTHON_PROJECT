from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

str = "가나다라마바사아자차";
arr_wf=[
    {'w':'100','f':0},
    {'w':'100','f':1},
    {'w':'100','f':2},
    {'w':'100','f':3},
    {'w':'100','f':4},
    {'w':'100','f':5},
    {'w':'100','f':6},
    {'w':'100','f':7},
    {'w':'600','f':0},
    {'w':'600','f':1},
    {'w':'600','f':2},
    {'w':'600','f':3},
    {'w':'600','f':4},
    {'w':'600','f':5},
    {'w':'600','f':6},
    {'w':'600','f':7}
    ]
driver = webdriver.Firefox()

for i in range(10):
    mychar=str[i:i+1]
    for idx,j in enumerate(arr_wf):
        driver.get("http://127.0.0.1:5000/?char={}&w={}&f={}".format(mychar,j['w'],j['f']))
        # driver.save_screenshot("임시.png")
        obj_span = driver.find_element(By.TAG_NAME, 'span')  
        
        element_png = obj_span.screenshot(f"{mychar}{idx}.png")
        driver.implicitly_wait(1)