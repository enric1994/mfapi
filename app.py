#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def test():
    return 'test ok'

app.run(host="0.0.0.0", port=5000)