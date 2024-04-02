import tensorflow as tf
import numpy as np
from day01.daomenu import DaoMenu
from day01.daodiet import DaoDiet
import datetime
from day01.daorecom import DaoRecom
from day01.daoemp import DaoEmp

class AaoRecom:
    def __init__(self,e_id):
        
        self.e_id = e_id
        self.dm = DaoMenu()
        self.dd = DaoDiet()
        self.dr = DaoRecom()
        
        
        self.lables = self.dm.getLabels()
        print(self.lables)
        self.x_train = None
        self.y_train = None
        
        self.cnt = self.dm.getCnt()
        self.setXYTrain(self.e_id,self.cnt)
        
    
    def setXYTrain(self,e_id,cnt):
        self.x_train,self.y_train = self.dd.getXtYt(e_id, cnt)
        
    
    def pred(self):
        
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(self.cnt*2,)),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(self.cnt, activation=tf.nn.softmax)
        ])
        
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        
        model.fit(self.x_train, self.y_train, epochs=10)
        model.save('recom.h5')
        
        
        pred = model.predict(self.x_train)
        
        for p in pred:
            myidx = np.argmax(p)
            print("myidx",myidx,p)
        
        x_rf = self.dd.getPred(self.e_id, self.cnt)
        
        print("x_rf",x_rf)
            
        pred_rf = model.predict(x_rf)
        myidx = np.argmax(pred_rf)
        recom_menu = self.lables[myidx]['m_name']
        recom_m_id = self.lables[myidx]['m_id']
        
        
        now = datetime.datetime.now()
        ymd = now.strftime("%Y%m%d")
        
        
        cnt = self.dr.insert(self.e_id, ymd, recom_m_id)
        
        print("e_id",self.e_id)
        print("recom_m_id",recom_m_id)
        print("ymd",ymd)
        print("cnt",cnt)
        
        
        print("myidx",myidx)
        print("recom_menu",recom_menu)

    
    def __del__(self):
        print("소멸자")


if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    
    for e in list:
        e_id = e['e_id']
        ar = AaoRecom(e_id)
        ar.pred()

