#!/usr/bin/env python
# coding:utf-8

from flask import Flask, session, redirect, url_for, escape, request, render_template
import uuid

app = Flask(__name__)

@app.route('/')
def index():
   if 'username' in session:
      return render_template('index.html', username = session['username'])
   session['uid'] = uuid.uuid4()
   return render_template('index.html', username = None)

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       session['username'] = request.form['username']
       return redirect(url_for('index'))
   return render_template('login.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

app.config['SECRET_KEY'] = str(uuid.uuid4())

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=80)
