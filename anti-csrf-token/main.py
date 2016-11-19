#!/usr/bin/env python
# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

@app.before_request
def csrf_protection():
   if request.method == "POST":
      token = session.pop('_csrf_token', None)
         if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
   session['_csrf_token'] = uuid.uuid4()
   return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=80)
