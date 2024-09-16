from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
@cross_origin()
def hello():
    data = {'message': 'hello Flask'}
    return jsonify(data)