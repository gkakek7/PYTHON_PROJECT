import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QMessageBox
from conda.common._logic import TRUE


form_class = uic.loadUiType("myomok02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D =[]
        self.flag_wb=True;
        self.flag_ing=True;
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.clicked.connect(self.myclick)
                btn.setToolTip("{},{}".format(i,j))
                line.append(btn)
            self.pb2D.append(line)
                
        self.show()
        self.myrender()
        
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j]==0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j]==1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j]==2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    
    
    def myclick(self) :
        if not(self.flag_ing):
            return
        str_ij=self.sender().toolTip()
        arr_ij=str_ij.split(",")
        i=int(arr_ij[0])
        j=int(arr_ij[1])
        if self.arr2D[i][j]>0:
            return
        stone=0
        if self.flag_wb:
            self.arr2D[i][j]=1
            stone=1
        else:
            self.arr2D[i][j]=2
            stone=2
            
        self.myrender()
        self.flag_wb=not(self.flag_wb)
        
        UP = self.getUP(i,j,stone);
        DW = self.getDW(i,j,stone);
        LE = self.getLE(i,j,stone);
        RI = self.getRI(i,j,stone);
        
        UR = self.getUR(i,j,stone);
        UL = self.getUL(i,j,stone);
        DR = self.getDR(i,j,stone);
        DL = self.getDL(i,j,stone);
        print(UP)
        print(DW)
        print(LE)
        print(RI)
        print(UR)
        print(UL)
        print(DR)
        print(DL)
        
        d1=UP+DW+1;
        d2=LE+RI+1;
        d3=UR+DL+1;
        d4=DR+UL+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            vic="";
            if self.flag_wb:
                vic="백";
            else :
                vic="흑";
            self.flag_ing=not(self.flag_ing)
            QMessageBox.about(self, "승리", vic+"돌 승리")
        
        
                
    def myreset(self) :
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j]=0
                
        self.myrender()
        self.flag_ing=True
        self.flag_wb=True


    def getUP(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                i=i-1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
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
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except :
            return cnt;
    def getRI(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                j+=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
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
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    
    def getUL(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i-=1
                j-=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
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
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
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
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
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
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;   
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    