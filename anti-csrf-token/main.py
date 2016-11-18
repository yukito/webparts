#!/usr/bin/env python
# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def set_csrf_protection():
   if request.method == "POST":

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=80)
