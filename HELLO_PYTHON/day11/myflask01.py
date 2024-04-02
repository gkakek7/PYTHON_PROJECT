from flask import Flask, redirect
from flask.json import jsonify
from flask.globals import request
from day11.daomember import Daomem

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('static/ajax.html')
    
@app.route('/mem_list', methods=["POST"])
def mem_list():
    de = Daomem();
    list = de.selectList()
    return jsonify(list=list)

@app.route('/mem_one', methods=["POST"])
def mem_one():
    data = request.get_json()
    m_id = data['m_id']
    de = Daomem()
    vo = de.select(m_id)
    return jsonify(vo=vo)

@app.route('/mem_add', methods=["POST"])
def mem_add():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    mobile = data['mobile']
    email = data['email']

    de = Daomem()
    cnt = de.insert(m_id, m_name, mobile, email)
    return jsonify(cnt=cnt)

@app.route('/mem_mod', methods=["POST"])
def mem_mod():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    mobile = data['mobile']
    email = data['email']

    de = Daomem()
    cnt = de.update(m_id, m_name, mobile, email)
    return jsonify(cnt=cnt)

@app.route('/mem_del', methods=["POST"])
def mem_del():
    data = request.get_json()
    m_id = data['m_id']
    print(m_id)
    de = Daomem()
    cnt = de.delete(m_id)
    print(cnt)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True) #이거 붙이면 서버 껐다 켰다 안해도 됨