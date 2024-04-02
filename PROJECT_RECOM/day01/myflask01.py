from flask import Flask,jsonify
import tensorflow as tf
import numpy as np
from flask.globals import request
from flask.templating import render_template
import pymysql
from day01.daonews import DaoNews

model = tf.keras.models.load_model('news_recom.h5')
app = Flask(__name__)
app.config['JSON_AS_ASCII']=False
dn = DaoNews()
@app.route('/')
def main():
    age = request.args.get('age')
    gen = request.args.get('gen')
    dept = request.args.get('dept')
    original_list=[[age,gen,dept]]
    recom=np.array([[int(cell) for cell in row] for row in original_list])
    pred=model.predict(recom)
    
    # 1순위 2순위 3순위 뽑기
    print(pred)
    idx1=np.argmax(pred[0])
    pred[0][idx1]=0
    idx2=np.argmax(pred[0])
    pred[0][idx2]=0
    idx3=np.argmax(pred[0])
    
    # 순위별 데이터 조회
    category = str(idx1)
    name1=dn.selectRecomName(category)
    url1 = dn.selectUrlList(category)
    
    category = str(idx2)
    name2=dn.selectRecomName(category)
    url2 = dn.selectUrlList(category)
    
    category = str(idx3)
    name3=dn.selectRecomName(category)
    url3 = dn.selectUrlList(category)
    
    # 조회된 데이터 json 형태 만들기
    result_dict1 = {'category': name1, 'url': url1}
    result_dict2 = {'category': name2, 'url': url2}
    result_dict3 = {'category': name3, 'url': url3}
    result = {'1':result_dict1,'2':result_dict2,'3':result_dict3}
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    