#!/usr/bin/env python3

from flask import g
import psycopg2
from este.paste_format import format_paste

def get_db():
    if not hasattr(g, 'db'):
        g.db = psycopg2.connect('dbname=este user=sakjur')
    return g.db

def fetch_paste(pastename, raw_only=False):
    db = get_db()
    cur = db.cursor()

    cur.execute('SELECT id, created, expires, lang, raw, highlight ' +
            'FROM pastes WHERE id = %s', [pastename])
    data = cur.fetchone()

    if data == None:
        cur.close()
        return None
    
    paste_id, created, expires, lang, raw, highlight = data

    if highlight == None and not raw_only:
        highlight = format_paste(raw, lang)
        cur.execute('UPDATE pastes SET highlight = %s WHERE id = %s',
                [highlight, pastename])
        db.commit()

    cur.close()

    return {'name': pastename,
            'size': len(raw),
            'lang': lang,
            'raw': raw,
            'content': highlight}

