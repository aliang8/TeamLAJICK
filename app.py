#import flask
import os
from flask import Flask, render_template, session, redirect, url_for, request
from utils import functions, login
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'life^2'

@app.route("/", methods=['POST','GET'])
def root():
    return render_template('dashboard.html', logged = 0)
    
@app.route("/<message>", methods=['POST','GET'])
def home(message):
    return render_template('dashboard.html', logged = 1, message=message)
    '''
    if session.get('username') != None:
        user = session.get('username')
        userInfo = functions.getUserInfo(user)
        #Check for all ajax requests here
        #All of POST type
        if request.method == 'POST':
           
            multi_dict = request.args
            for key in multi_dict:
                print multi_dict.get(key)
                print "1"
           
            if "addToDo" in request.form:
                print request.form.get("addToDo")
                return functions.insertToDo(user, request.form.get("addToDo"))
            print "Bad"
            if "addHabit" in request.form:
                return functions.insertHabit(user, request.form.get("addHabit"))
            if "addGoal" in request.form:
                return functions.insertGoal(user, request.form.get("addGoal"))
            
    
    
        #If not a request, load everything
        todos = functions.getUserToDos(user)
        habits = functions.getUserHabits(user)
        goals = functions.getUserGoals(user)

        gold = functions.getUserInfo(user)[1]
        
        return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance = gold)
    
    '''


@app.route("/authenticate/", methods = ['POST','GET'])
def authenticate():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        hashpass = hashlib.sha224(password).hexdigest()
        if 'login' in request.form:
            if login.login(username,password):
                session['username'] = username
                return redirect(url_for("home",message = "Login successful"))
            else:
                return redirect(url_for("home",message = "Login failed"))
        else:
            if login.register(username,password):
                return redirect(url_for("home",message = "Registration successful"))
            else:
                return redirect(url_for("home",message = "Registration failed"))

@app.route("/logout/", methods=['POST','GET'])
def logout():
    session.pop('username')
    return redirect(url_for("home",message = "Logout successful"))

if __name__ == "__main__":
    app.debug = True
    login.initializeTables()
    app.run()
