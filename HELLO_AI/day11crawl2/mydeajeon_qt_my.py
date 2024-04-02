import sys
import json
from selenium import webdriver
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium.webdriver.common.by import By

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("mydeajeon_qt_my.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Firefox()
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.driver.get("http://traffic.daejeon.go.kr/")

    def pbFunction(self):
        try:
            input=self.driver.find_elements(By.CSS_SELECTOR,'input[type="hidden"]')
            for idx,i in enumerate(input):
                if isinstance(i.get_attribute("value"), int):
                    continue
                jsonData=json.loads(i.get_attribute("value"));
                if isinstance(jsonData, int):
                    continue
                print(jsonData["gpsLati"])
                print(jsonData["gpsLong"])
                
        
        except Exception as e:
            print(e)        
            
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()