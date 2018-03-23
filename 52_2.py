# -*- coding: utf-8 -*-

"""

filename: time alarm service flask
date: 2018-03-23
purpose: flask web server in local

"""
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/application/json')
def cur_time():
    date = str(datetime.datetime.now())
    date_dict = {}
    date_dict["curtime"] = date.split('.')[0]
    json = str(date_dict)
    return json


if __name__ == "__main__":
    app.run()