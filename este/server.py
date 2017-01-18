#!/usr/bin/env python3

from flask import Flask, render_template, Response, abort
from este.paste_db import get_paste

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/p/<paste_id>')
def paste(paste_id):
    data = get_paste(paste_id)
    if data == None:
        return abort(404)
    return render_template('paste.html', paste=data)

@app.route('/raw/<paste_id>')
def raw(paste_id):
    data = get_paste(paste_id)
    if data == None:
        return abort(404)
    return Response(data['raw'], mimetype='text/plain')

if __name__ == '__main__':
    app.run()

