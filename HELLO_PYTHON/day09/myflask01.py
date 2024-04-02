from flask import Flask
from flask.globals import request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello woong!'

if __name__ == '__main__':
    app.run(debug=True) #이거 붙이면 서버 껐다 켰다 안해도 됨