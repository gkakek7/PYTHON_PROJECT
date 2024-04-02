import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import QPushButton, QIcon, QPixmap

form_class = uic.loadUiType("./myomock01.ui")[0]
class WindowClass(QMainWindow, form_class):
    flag_wb=True
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb=[[]]
        for i in range(0,9+1):
            for j in range(0,9+1):
                pass
    def myclick(self):
        if self.flag_wb:
            icon = QIcon("1.png")
            self.pb.setIcon(icon)
            self.flag_wb=not(self.flag_wb)
        else :
            icon = QIcon("2.png")
            self.pb.setIcon(icon)
            self.flag_wb=not(self.flag_wb)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    sys.exit(app.exec_())