"""
A simple chatting application made using flask backend and uses AJAX Polling
"""

import datetime
import time
import os
from flask import Flask, render_template, request, session, escape

app = Flask(__name__)
app.secret_key = 'MadeByViresh'


@app.route('/')
def form():
    n = ''
    if 'name' in session:
        n = escapes(session['name'])
    f2 = open('chat.txt', 'r')
    l = []
    for lines in f2:
        l.append(lines)
    f2.close()
    return render_template('home.html', li=l, name=n)


@app.route('/', methods=['POST'])
def sendText():
    if request.method == 'POST':
        session['name'] = request.form['name']
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    name = request.form['name']
    t = request.form['message']
    file = open('chat.txt', 'a')
    file.write(st + '  ' + name + ' : ' + t + '\r\n')
    file.close()
    return render_template('home.html', name=name)


@app.route('/chat/')
def info():
    f = open('chat.txt', 'r')
    return render_template('texttempl.html', content=f.read())


port = int(os.getenv('VCAP_APP_PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
