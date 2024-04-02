
from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/param')
def param():
    menu = request.args.get('menu')
    return 'PARAM:'+menu

@app.route('/post', methods=['POST'])
def post():
    menu = request.form["menu"]
    return 'POST:'+menu

@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치","일지매"]
    c = [
        {'e_id':1,'e_name':1,'gen':1,'addr':1},
        {'e_id':2,'e_name':2,'gen':2,'addr':2},
        {'e_id':3,'e_name':3,'gen':3,'addr':3}
    ]
    return render_template("forw.html", a=a, b=b, c=c)

@app.route('/emp')
def emp():
    conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from emp'
    curs.execute(sql)
    emps = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("emp.html",emps=emps)

if __name__ == '__main__':
    app.run(debug=True) #이거 붙이면 서버 껐다 켰다 안해도 됨