from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys

from_class = uic.loadUiType("myqt03.ui")[0]


class MainClass(QMainWindow, from_class):

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setupUi(self)
        
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
        a = self.le1.text()
        b = self.le2.text()
        c = int(a) - int(b)
        self.le3.setText(str(c))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()
