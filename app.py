# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:36:13 2019

@author: vaishnov
"""

from flask import Flask

UPLOAD_FOLDER = 'E:\\ML\\elction roll\\'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024