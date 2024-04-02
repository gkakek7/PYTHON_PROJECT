import sys
import json
from selenium import webdriver
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium.webdriver.common.by import By
from day12kakao.dao_bus_path import DaoBusPath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("mydeajeon_qt.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Firefox()
        self.dbp=DaoBusPath()
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.pb2.clicked.connect(self.pb2Function)
        self.driver.get("http://traffic.daejeon.go.kr/")

    def pb2Function(self):
        try:
            lis = WebDriverWait(self.driver, 2).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.route > li'))
            )
            for idx,li in enumerate(lis):
                time.sleep(10)
                lli=self.driver.find_element(By.CSS_SELECTOR, "#root > div.mapWrap > aside > div > article > div > ul > li:nth-child("+str(idx+1)+")")
                lis[idx].click()
                self.pbFunction()
                self.driver.refresh()
                time.sleep(1)
                self.driver.back()
                self.driver.refresh()
                time.sleep(1)
                # 대기 조건 변경
                WebDriverWait(self.driver, 2).until(
                    EC.staleness_of(li)
                )
        except Exception as e:
                print("pb2",e)  
    def pbFunction(self):
        try:
            # 버스 번호 엘리먼트까지 기다림
            strong = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'strong[class="bus_no"]'))
            )
            
            mark = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.bus_type'))
            )
            
            spans = WebDriverWait(self.driver, 2).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class="st_id"]'))
            )
            time.sleep(1)
            for idx, s in enumerate(spans):
                try:
                    myparent = s.find_element(By.XPATH, '..')
                    sp2 = myparent.find_elements(By.CSS_SELECTOR, "span[class='st_name']")
    
                    bus_id = s.text
                    bus_name = sp2[0].text
    
                    ip = myparent.find_elements(By.CSS_SELECTOR, "input")[0]
                    txt = ip.get_attribute("value")
    
                    myjson = json.loads(txt)
                    lat = myjson['gpsLati']
                    lng = myjson['gpsLong']
    
                    cnt = self.dbp.insert(mark.text+strong.text, idx, bus_id, bus_name, lat, lng)
                    print(mark.text+strong.text, idx, bus_id, bus_name, lat, lng, cnt)
    
                except Exception as e:
                    print(e)
    
        except Exception as e:
            print("Error waiting for bus number:", e)   
                
            
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()