import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import json
from day15crawl.dao_bus_path import DaoBusPath


form_class = uic.loadUiType("my_daejeon_all_qt.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.dbp = DaoBusPath()
        self.driver = webdriver.Firefox()
        self.bp_names=[]
        self.cnt=0;
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.pb_all.clicked.connect(self.my_bussall)
        self.pb_macro.clicked.connect(self.my_macro)
        self.show()
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        self.my_bussall()
        
    def my_macro(self):
        lis = self.driver.find_elements(By.CSS_SELECTOR,".route > li")
        lis[self.cnt].click()
        time.sleep(2)
    
    def my_bussall(self):
        ul = self.driver.find_element(By.CSS_SELECTOR,"ul[class='route']")
        marks=ul.find_elements(By.CSS_SELECTOR, "mark")
        strongs=ul.find_elements(By.CSS_SELECTOR, "strong")
        self.bp_names.clear()
        for idx,mark in enumerate(marks):
            bp_name="{}{}".format(mark.text,strongs[idx].text)
            self.bp_names.append(bp_name)
            print(idx,mark.text,strongs[idx].text)
        print(self.bp_names)
        print(len(self.bp_names))
        
        
    def myclick(self) :
        try:
            for i in self.bp_names:
                self.my_macro()
                spans = self.driver.find_elements(By.CSS_SELECTOR,"span[class='st_id']")
                
                for idx,s in enumerate(spans):
                    
                    myparent = s.find_element(By.XPATH, '..')
                    sp2 = myparent.find_elements(By.CSS_SELECTOR,"span[class='st_name']")
                    
                    bus_id = s.text
                    bus_name = sp2[0].text
                    
                    ip = myparent.find_elements(By.CSS_SELECTOR,"input")[0]
                    txt = ip.get_attribute('value')
                    
                    myjson=json.loads(txt)
                    lat = myjson['gpsLati']
                    lng = myjson['gpsLong']
                    cnt = self.dbp.insert(self.bp_names[self.cnt], idx, bus_id, bus_name, lat, lng)
                    print(self.bp_names[self.cnt], idx, bus_id, bus_name, lat, lng,cnt)
                self.cnt+=1
                self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
                time.sleep(2)
        except Exception as e:
            print(e)
            
            
            
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()