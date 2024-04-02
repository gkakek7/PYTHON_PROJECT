from flask import Flask, request,redirect,render_template
from flask_cors.extension import CORS
import os
from flask.json import jsonify
from random import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return redirect("record")

@app.route('/record')
def record():
    return render_template('record.html')


@app.route('/mic_recodrd_upload.ajax', methods=['POST','GET'])
def login():
    file = request.files.get('file')
    print("file",file)
    file.save(file.filename)
    return jsonify(result = "success2")


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(ssl_context='adhoc')
    
    