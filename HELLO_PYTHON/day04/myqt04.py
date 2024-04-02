from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys

from_class = uic.loadUiType("myqt04.ui")[0]


class MainClass(QMainWindow, from_class):

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setupUi(self)
        
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
        a = self.te.toPlainText()
        aa = int(a)
        txt = "";
        
        for i in range(1,9+1) :
            txt += "{}*{}={}\n".format(aa,i,aa*i)
            
        self.pte.setPlainText(txt)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()
