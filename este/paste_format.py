#!/usr/bin/env python3

from pygments import highlight
import pygments.lexers as lex
from pygments.formatters import HtmlFormatter

LEXERS = {
    'erlang': lex.ErlangLexer,
    'python': lex.PythonLexer,
}

def format_pasteline(line):
    if line == '':
        return '<li><br /></li>'

    init_space = 0
    for char in line:
        if char == ' ':
            init_space += 1
        else:
            break

    return '<li>{}{}</li>'.format('&nbsp;' * init_space, line.lstrip())


def format_paste(raw, lang='plain'):
    lexer = LEXERS.get(lang, lex.TextLexer)(tabsize=4)
    data = highlight(raw, lexer, HtmlFormatter(nowrap=True))
    arr = map(format_pasteline, data.split('\n'))
    return "\n".join(arr)

