
from flask import Flask, redirect
from flask.globals import request
from flask.templating import render_template
import pymysql

app = Flask(__name__)


@app.route('/')
@app.route('/ganada')
def ganada():
    farr = ["Nanum Myeongjo",
            "Nanum Gothic",
            "Nanum Pen Script",
            "Black Han Sans",
            "Sunflower",
            "Dokdo",
            "Stylish",
            "Gaegu"]
    
    f = request.args.get('f')
    char = request.args.get('char')
    w = request.args.get('w')
    ff=farr[int(f)]
    return render_template("ganada.html", char=char, w=w, f=ff)

@app.route('/static/examples/_ex99')
def threejs():
    i = request.args.get('i')
    rx = request.args.get('rx')
    ry = request.args.get('ry')
    return render_template("_ex99.html",i=i,rx=rx,ry=ry)

if __name__ == '__main__':
    app.run(debug=True)  # 이거 붙이면 서버 껐다 켰다 안해도 됨
