from flask import Flask
from flask import render_template,url_for
from flask.globals import request
import backend

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        if backend.IsUser(request.form['Username'],request.form['Password']):
            return render_template('notes.html',result=request.form['Username'])
        else:
            return render_template('login.html',result=False)
    else:
        return render_template('login.html')

@app.route('/SucessfulLogin')
def SucessfulLogin():
    return render_template('SucessfulLogin.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='POST':
        if backend.AddUser(request.form['Username'],request.form['Password']):
            print("phase1")
            return render_template('SuccessFullReg.html')
        else:
            return render_template('register.html',result=backend.AddUser(request.form['Username'],request.form['Password']))
    else:
        print("phase2")
        return render_template('register.html')

@app.route('/SuccessFullReg')
def SuccessFullReg():
    return render_template('SuccessFullReg.html')

if __name__=="__main__":
    app.run()