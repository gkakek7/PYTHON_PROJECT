import sys
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QApplication, QMessageBox
from PyQt5.Qt import QPushButton, QIcon, QPixmap, QMessageBox

form_class = uic.loadUiType("./myomock02hw.ui")[0]

class WindowClass(QMainWindow, form_class):
    arr2D = [
        [0,0,0,0,0, 0,0,0,0,0],#1
        [0,0,0,0,0, 0,0,0,0,0],#2
        [0,0,0,0,0, 0,0,0,0,0],#3
        [0,0,0,0,0, 0,0,0,0,0],#4
        [0,0,0,0,0, 0,0,0,0,0],#5
                                                   
        [0,0,0,0,0, 0,0,0,0,0],#6
        [0,0,0,0,0, 0,0,0,0,0],#7
        [0,0,0,0,0, 0,0,0,0,0],#8
        [0,0,0,0,0, 0,0,0,0,0],#9
        [0,0,0,0,0, 0,0,0,0,0]#10
        ]
    flag_wb=True
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.rand()
        self.show()
        
    def myclick(self):
        bt=self.sender()
        btn_ij=bt.toolTip()
        ij=btn_ij.split(",")
        i=int(ij[0])
        j=int(ij[1])
        if self.flag_wb:
            stone=1;
            icon = QIcon("1.png")
            bt.setIcon(icon)
            self.arr2D[i][j]=1;
        else :
            stone=2;
            icon = QIcon("2.png")
            bt.setIcon(icon)
            self.arr2D[i][j]=2;
        self.flag_wb=not(self.flag_wb)
        
        self.rand()
        up = self.getUP(i,j,stone);
        dw = self.getDW(i,j,stone);
        le = self.getLE(i,j,stone);
        ri = self.getRI(i,j,stone);
        
        ur = self.getUR(i,j,stone);
        ul = self.getUL(i,j,stone);
        dr = self.getDR(i,j,stone);
        dl = self.getDL(i,j,stone);
        
        d1=up+dw+1;
        d2=le+ri+1;
        d3=ur+dl+1;
        d4=dr+ul+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            vic="";
            if self.flag_wb:
                vic="백";
            else :
                vic="흑";
                msg_box = QMessageBox.warning(None, "승리", vic+"돌 승리")
    def rand(self):
        for i in range(10):
            for j in range(10):
                btn=QPushButton("",self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40,i*40,40,40))
                btn.clicked.connect(self.myclick)
                btn.setToolTip(str(i)+","+str(j))
                
                
    def getUP(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                i=i-1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    def getRI(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                j+=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    def getLE(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                j-=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    def getDW(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
    def getUL(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i-=1
                j-=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
        
    def getUR(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i-=1
                j+=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
    def getDL(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                j-=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
    def getDR(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                j+=1
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    sys.exit(app.exec_())