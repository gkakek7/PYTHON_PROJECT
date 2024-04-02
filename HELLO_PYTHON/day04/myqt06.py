import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        
        mine = self.le_mine.text()
        com = random()
        
        if com <= 0.5:
            comm="짝"
        else:
            comm="홀"
            
        print(comm)
        print(com)
        self.le_com.setText(comm)
        
        if comm==mine:
            result = "ㅊㅊ 이김"
        else:
            result = "ㅠㅠ 짐"
        self.le_result.setText(result)
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()