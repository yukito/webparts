#!/usr/bin/env python
# coding:utf-8

from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response
import os

app = Flask(__name__)

path = os.getcwd()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/list/')
@app.route('/list/<path_name>')
def listing(path_name = ''):
   print path_name
   file_list = os.listdir(path + '/' +path_name)
   return render_template('listing.html', path = path + '/' + path_name, file_list = file_list)

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=80)
