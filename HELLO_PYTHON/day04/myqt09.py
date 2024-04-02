import sys

from Cython.Compiler.Naming import self_cname
from PyQt5 import uic
from PyQt5.Qt import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt09.ui")[0]


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)
        self.telNum = ""
        
    def mycall(self):
        print("전화를 겁니다.")
        QMessageBox.about(self, "CALL...", self.telNum + "에게 전화를 겁니다..")

    def myclick(self):
        sender_button = self.sender()
        button_text = sender_button.text()
        # print(f"Button '{button_text}' was clicked")
        self.telNum += button_text
        self.le.setText(self.telNum);


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()