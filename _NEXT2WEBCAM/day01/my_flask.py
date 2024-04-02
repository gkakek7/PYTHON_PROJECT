from flask import Flask, request,redirect
from flask_cors.extension import CORS
import os
from flask.json import jsonify
from random import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return redirect("static/capture.html")


@app.route('/cam_capture_upload.ajax', methods=['POST','GET'])
def login():
    mem_id = request.form.get('mem_id')
    file = request.files.get('file')
    
    print("mem_id",mem_id)
    print("file",file)
    file.save(file.filename+str(random()))
    return jsonify(result = "success2")


if __name__ == '__main__':
    app.run(debug=True)
    
    