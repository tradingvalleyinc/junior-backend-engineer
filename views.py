from run import app
from flask import jsonify

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

