#!/usr/bin/env python3

from pygments import highlight
from pygments.lexers import PythonLexer, ErlangLexer, TextLexer
from pygments.formatters import HtmlFormatter

def format_pasteline(line):
    if line == '':
        return '<li><br /></li>'

    init_space = 0
    for char in line:
        if char == ' ':
            init_space += 1
        elif char == '\t':
            init_space += 4
        else:
            break

    return '<li>{}{}</li>'.format('&nbsp;' * init_space, line.lstrip())


def format_paste(raw, lang='plain'):
    lexer = TextLexer()
    if lang == 'python':
        lexer = PythonLexer()
    elif lang == 'erlang':
        lexer = ErlangLexer()
    data = highlight(raw, lexer, HtmlFormatter(nowrap=True))

    arr = map(format_pasteline, data.split('\n'))

    return "".join(arr)

