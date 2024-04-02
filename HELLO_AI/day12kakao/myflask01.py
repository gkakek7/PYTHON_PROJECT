from flask import Flask ,redirect
from flask.globals import request
from flask.templating import render_template
import pymysql
import requests
from day12kakao.dao_bus_path import DaoBusPath
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('static/bus_deajeon.html')
@app.route('/bus')
def bus():
    return render_template("bus.html")

@app.route('/bp_list')
def ajax():
    dbp=DaoBusPath()
    list=dbp.selectList()
    print(list)
    return jsonify(list=list)
if __name__ == '__main__':
    app.run(debug=True) #이거 붙이면 서버 껐다 켰다 안해도 됨