import sys
from selenium import webdriver
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium.webdriver.common.by import By

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myselenium_qt.ui")[0]

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
        self.driver.get("https://map.kakao.com/")

    def pbFunction(self):
        try:
            strongs=self.driver.find_elements(By.CSS_SELECTOR,'strong[class="busstop"]')
            for idx,s in enumerate(strongs):
                obj_sele_s=s.find_element(By.XPATH,'..')
                obj_busstop=obj_sele_s.find_elements(By.CSS_SELECTOR,'p[class="busid"]')
                print(idx,obj_busstop[0].text)
        except Exception as e:
            print(e)
                
            
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()