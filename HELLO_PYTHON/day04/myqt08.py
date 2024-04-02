import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt08.ui")[0]

class MainClass(QMainWindow, form_class):
    com = int(random()*99)
    
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        mine = self.le.text()
        mm = int(mine)
        str_new = ""
        
        if mm < self.com:
            str_new = str(mm)+"보다 UP\n"
        elif mm > self.com :
            str_new = str(mm)+"보다 DOWN\n"
        else:
            str_new= str(mm)+"정답\n"
            
        str_old = self.pte.toPlainText()
        
        self.pte.setPlainText(str_new+str_old)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()