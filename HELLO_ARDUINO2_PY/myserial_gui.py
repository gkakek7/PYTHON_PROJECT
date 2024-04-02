import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myserial_gui.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.my_serial = serial.Serial(port='COM4',baudrate=9600)
        self.setupUi(self)
        self.pb_on.clicked.connect(self.my_on)  
        self.pb_off.clicked.connect(self.my_off)   
  

    def my_on(self):
        self.my_serial.write("a\n".encode())
    def my_off(self):
        self.my_serial.write("b\n".encode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()