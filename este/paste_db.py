#!/usr/bin/env python3

from pygments import highlight
from pygments.lexers import PythonLexer, ErlangLexer
from pygments.formatters import HtmlFormatter

xyz = """#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/p/<paste_id>')
def paste(paste_id):
    return render_template('paste.html', paste_id=paste_id)

if __name__ == '__main__':
    app.run()

"""

erl = """
-module(stack).

-export([pow/2]).

prod(N, K) when K < N -> prod_(N, 0, K);
prod(N, K) -> prod_(K, 0, N).

prod_(_, Sum, 0) -> Sum;
prod_(N, Sum, K) -> prod_(N, Sum+N, K-1).

pow(_, 0) -> 1;
pow(N, K) -> prod(N, pow(N, K - 1)).

"""

def get_paste(pastename):
    paste = None
    if pastename == 'xyz':
        paste = {'lang': 'python', 'file': xyz}
    elif pastename == 'erl':
        paste = {'lang': 'erlang', 'file': erl}
    if paste:
        if paste['lang'] == 'python':
            lexer = PythonLexer()
        elif paste['lang'] == 'erlang':
            lexer = ErlangLexer()
        else:
            lexer = None
        if lexer:
            data = highlight(paste['file'], lexer, HtmlFormatter(nowrap=True))
        else:
            data = paste['file']
        arr = []


        for line in data.split('\n'):
            init_space = 0
            for char in line: 
                if char == ' ':
                    init_space += 1
                elif char == '\t':
                    init_space += 4
                else:
                    break
            arr.append('<li>{}{}</li>'.format('&nbsp;' * init_space, line.lstrip()))

        out = "".join(arr)

        return {'name': pastename,
                'size': len(paste['file']),
                'lang': paste['lang'],
                'raw': paste['file'],
                'content': out}
    return None

