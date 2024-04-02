import sys
import tensorflow as tf
import numpy as np

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt_recom.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.labels=[
            {'name':'짜장','label':0,'arr':[1,0,0,0,0]},
            {'name':'삼겹살','label':1,'arr':[0,1,0,0,0]},
            {'name':'전복죽','label':2,'arr':[0,0,1,0,0]},
            {'name':'킹크랩','label':3,'arr':[0,0,0,1,0]},
            {'name':'라면','label':4,'arr':[0,0,0,0,1]}
            ]
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.model = tf.keras.models.load_model('recom.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        pred_rf=None
        
    def getIdxByName(self,name):
        for idx,l in enumerate(self.labels):
            if name == l['name']:
                return idx
        return -1
    def pbFunction(self):
        myname=self.le.text()
        idx=self.getIdxByName(myname)
        
        x_rf = np.array([
            self.labels[idx]['arr']
        ])
        pred_rf=self.model.predict(x_rf)
        myidx=np.argmax(pred_rf)
        menu=self.labels[myidx]['name']
        self.le_recom.setText(menu)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()