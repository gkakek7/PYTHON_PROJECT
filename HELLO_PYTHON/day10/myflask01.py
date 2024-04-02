from flask import Flask, redirect
from flask.json import jsonify
from flask.globals import request
from day10.daoemp import DaoEmp

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('static/ajax.html')
    # return '<script>location.href="static/ajax.html"</script>'#이것도 같은 결과를 가져옴
    
@app.route('/ajax', methods=["POST"])
def ajax():
    data = request.get_json()
    print(data['menu']) #짬뽕하나만 가져오는 것
    return jsonify(result="success")
    
@app.route('/emp_list', methods=["POST"])
def emp_list():
    de = DaoEmp()
    list = de.selectList()
    return jsonify(list=list)

@app.route('/emp_one', methods=["POST"])
def emp_one():
    data = request.get_json()
    e_id = data['e_id']
    de = DaoEmp()
    vo = de.select(e_id)
    return jsonify(vo=vo)

@app.route('/emp_add', methods=["POST"])
def emp_add():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']

    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return jsonify(cnt=cnt)

@app.route('/emp_mod', methods=["POST"])
def emp_mod():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']

    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return jsonify(cnt=cnt)

@app.route('/emp_del', methods=["POST"])
def emp_del():
    data = request.get_json()
    e_id = data['e_id']
    print(e_id)
    de = DaoEmp()
    cnt = de.delete(e_id)
    print(cnt)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True) #이거 붙이면 서버 껐다 켰다 안해도 됨