CREATE TABLE pastes (
    id VARCHAR(32) PRIMARY KEY,
    created TIMESTAMP DEFAULT (now() AT TIME ZONE 'utc'),
    expires TIMESTAMP,
    lang VARCHAR(32),
    raw TEXT NOT NULL,
    highlight TEXT
);

INSERT INTO pastes (id, lang, raw) VALUES
('erl', 'erlang', '-module(stack).

-export([pow/2]).

prod(N, K) when K < N -> prod_(N, 0, K);
prod(N, K) -> prod_(K, 0, N).

prod_(_, Sum, 0) -> Sum;
prod_(N, Sum, K) -> prod_(N, Sum+N, K-1).

pow(_, 0) -> 1;
pow(N, K) -> prod(N, pow(N, K - 1)).'),
('xyz', 'python', '#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route(''/'')
def main():
    return render_template(''index.html'')

@app.route(''/p/<paste_id>'')
def paste(paste_id):
    return render_template(''paste.html'', paste_id=paste_id)

if __name__ == ''__main__'':
    app.run()')

