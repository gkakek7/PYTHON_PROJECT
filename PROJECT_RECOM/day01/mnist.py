import tensorflow as tf
import numpy as np
from day01.daonews import DaoNews
print(tf.__version__)
dn=DaoNews()
list=dn.selectXYLabelList();
cnt=dn.deleteRecome();
if cnt>0:
    
    print(list)
    cnt=dn.selectCnt()
    x_train = dn.selectList()
    y_train = dn.selectLabeList()   
    print(x_train)
    print(y_train)
    
    
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(3,)),
        tf.keras.layers.Dense(256, activation=tf.nn.relu),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(1024, activation=tf.nn.relu),
        tf.keras.layers.Dense(cnt, activation=tf.nn.softmax)
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=30)
    model.summary()
    model.save('news_recom.h5')
    arr=[]
    for i in range(5):
        for j in range(5):
            for k in range(2):
                arr.append([i, j, k])
    
    newarr=[]
    for i in arr:
        pred = model.predict(np.array([[i[0], i[1], i[2]]]).astype(float))
        
        idx1=np.argmax(pred[0])
        pred[0][idx1]=0
        idx2=np.argmax(pred[0])
        pred[0][idx2]=0
        idx3=np.argmax(pred[0])
        
        a1=[str(idx1),str(i[0]),str(i[1]),str(i[2]),"1"]
        newarr.append(a1)
        a2=[str(idx2),str(i[0]),str(i[1]),str(i[2]),"2"]
        newarr.append(a2)
        a3=[str(idx3),str(i[0]),str(i[1]),str(i[2]),"3"]
        newarr.append(a3)   
        
    print(newarr)
    cnt=0;
    for i in newarr:
        j=dn.insertRecom(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]))
        cnt=cnt+j
    
    
    # for i in newarr:
    #     j=dn.updateRecom(i[0], i[1], i[2], i[3], i[4])
    #     print(i[0], i[1], i[2], i[3], i[4])
    #     cnt=cnt+j
    # print(cnt)
