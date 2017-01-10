#import flask
from flask import Flask, render_template, session, redirect, url_for
from utils import functions, login
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '1'


@app.route()
def dashboard():
    return

@app.route("", methods = ['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']

        #Attempt to login
        if 'login' in request.form:
            if (login.login(username, password)):
                return #Success
            else:
                return #Fail

        #Attempt to register
        if 'register' in request.form:
            if (login.register(username, password)):
                return #Success
            else:
                return #Fail
            
    return

@app.route()
def logout():
    session.pop('username')
    return redirect(url_for())

@app.route()
def profile():
    return

if __name__ == "__main__":
    app.debug = True
    login.initializeTables()
    app.run()
