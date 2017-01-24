#import flask
from flask import Flask, render_template, session, redirect, url_for, request
from utils import functions, login
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'life^2'

@app.route("/", methods=['POST','GET'])
def new():
    return render_template('dashboard.html')

@app.route("/home/", methods=['POST','GET'])
def home(message):
    username = request.form['user']
    gold = functions.getUserInfo('j')[0]
    return render_template('dashboard.html',message=message, gold=gold)

@app.route("/authenticate/", methods = ['POST','GET'])
def authenticate():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        hashpass = hashlib.sha224(password).hexdigest()
        if 'login' in request.form:
            if login.login(username,password):
                session['username'] = username
                return redirect(url_for("home"))
            else:
                return redirect(url_for("home",message = "Login failed"))
        else:
            if login.register(username,password):
                return redirect(url_for("home",message = "Registration successful"))
            else:
                return redirect(url_for("home",message = "Registration failed"))

@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for("home",message = "Logout successful"))

if __name__ == "__main__":
    app.debug = True
    login.initializeTables()
    app.run()
