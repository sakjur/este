#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world\n'

@app.route('/p/<paste_id>')
def paste(paste_id):
    return render_template('paste.html', paste_id=paste_id)

if __name__ == '__main__':
    app.run()

