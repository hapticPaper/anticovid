import requests, os
import pandas as pd
import numpy as np
from flask import Flask, render_template, send_from_directory
from flask_restful import reqparse
import logging
#import queries as q


app=Flask(__name__)
SESS = requests.session()
app.secret_key='shuaasdtupdsafddgtashgfiagsghhasedgfcrdadgedftkeydohjjsdfntteagdasladadsgfdasfhyonewhatitis'










@app.route('/collect')
def collect():
    return render_template('/collect.html')



@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/apple-touch-icon.png')
def appletouch():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')



@app.route('/')
def home():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
