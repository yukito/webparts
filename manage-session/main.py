#!/usr/bin/env python
# coding:utf-8

from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response
import uuid
from lib.session import ManageSession

app = Flask(__name__)

session_list = {}

@app.route('/')
def index():
   if request.cookies.get('sessionid') in session_list:
      uid = request.cookies.get('sessionid')
      return render_template('index.html', username = session_list[uid].username)
   content = render_template('index.html')
   response = make_response(content)
   uid = str(uuid.uuid4())
   session_list[uid] = ManageSession()
   response.set_cookie('sessionid', value = uid, path = '/', httponly = True)
   return response

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      uid = str(uuid.uuid4())
      session_list[uid] = ManageSession()
      session_list[uid].username = request.form['username']
      content = redirect(url_for('index'))
      response = make_response(content)
      response.set_cookie('sessionid', value = uid, path = '/', httponly = True)
      return response
   return render_template('login.html')

@app.route('/logout')
def logout():
   uid = request.cookies.get('sessionid')
   session_list.pop(uid)
   return redirect(url_for('index'))

app.config['SECRET_KEY'] = str(uuid.uuid4())

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=80)
