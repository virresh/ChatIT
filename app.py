from flask import Flask,render_template,url_for,request,session,escape
import datetime
import time
app = Flask(__name__)

@app.route("/")
@app.route("/sendText")
def form():
    n=""
    if 'name' in session:
        n= escape(session['name'])
    f2 = open("thoughtlist.txt","r")
    l = []
    for lines in f2:
        l.append(lines)
    f2.close()
    return render_template('form_submit.html',li=l,name=n)

@app.route('/sendText', methods=['POST'])
def sendText():
    if request.method == 'POST':
        session['name'] = request.form['name']
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    name = request.form['name']
    t= request.form['thought']
    file = open("thoughtlist.txt","a")
    file.write(st + "  " + name + " : " + t + "\r\n")
    file.close()
    f2 = open("thoughtlist.txt","r")

    l = []
    for lines in f2:
        l.append(lines)
    f2.close()
    return render_template('form_submit.html',li=l,name=name)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True,port=8002,host='0.0.0.0')

