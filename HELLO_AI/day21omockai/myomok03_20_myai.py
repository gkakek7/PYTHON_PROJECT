import sys
import numpy as np
from tensorflow.keras.models import load_model
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QMessageBox
from conda.common._logic import TRUE
from _nsis import out


form_class = uic.loadUiType("myomok03_20_myai.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.gibo = [
                {'i':0,'j':0},
                {'i':1,'j':0},
                {'i':2,'j':0},
                {'i':3,'j':0},
                {'i':4,'j':0}
            ]
        self.model = load_model('omok.h5')
        self.gibo_cnt=0
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                   
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                   
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                   
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D =[]
        self.flag_wb=True;
        self.flag_ing=True;
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        for i in range(20):
            line = []
            for j in range(20):
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
        for i in range(20):
            for j in range(20):
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
       
        self.arr2D[i][j]=1
        stone=1
        
            
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
        # print(UP)
        # print(DW)
        # print(LE)
        # print(RI)
        # print(UR)
        # print(UL)
        # print(DR)
        # print(DL)
        
        d1=UP+DW+1;
        d2=LE+RI+1;
        d3=UR+DL+1;
        d4=DR+UL+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            if self.flag_wb:
                QMessageBox.about(self, "승리", "흑돌 승리")
                self.flag_ing=False
            
            
            
#==========================================================================================================
        

        if not(self.flag_ing):
            return
        myarr=[]
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j]==2:
                    myarr.append(-1)
                else:
                    myarr.append(self.arr2D[i][j])
       
        input=np.array(myarr)
        input=np.reshape(input,(1,20,20,1))
        print("input",input)
        print("input",input.shape)
        output = self.model.predict(input)
        out400=np.argmax(output[0])
        i=int(out400/20)
        j=out400%20
        self.arr2D[i][j]=2
        stone=2
        self.gibo_cnt+=1
        
        
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
        
        # print(UP)
        # print(DW)
        # print(LE)
        # print(RI)
        # print(UR)
        # print(UL)
        # print(DR)
        # print(DL)
        
        d1=UP+DW+1;
        d2=LE+RI+1;
        d3=UR+DL+1;
        d4=DR+UL+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            if self.flag_wb:
                self.flag_ing=not(self.flag_ing)
                QMessageBox.about(self, "승리", "백돌 승리")
           
        
                
    def myreset(self) :
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
                
        self.myrender()
        self.flag_ing=True
        self.flag_wb=True
        self.gibo_cnt=0


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
    
    
    
    
    
    
    
    
    
    
    
    
    