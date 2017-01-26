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
    lb = functions.getAllUserInfo('events_completed')
    return render_template('dashboard.html', logged = 0, lb=lb)
    
@app.route("/<message>", methods=['POST','GET'])
@app.route("/<message>/<sort>", methods=['POST','GET'])
def home(message,sort=None):
    if session.get('username') != None:
        user = session.get('username')
        userInfo = functions.getUserInfo(user)

        #Check for all ajax requests here
        #All of POST type
        gold = functions.getUserInfo(user)[1]
        if request.method == 'POST':
            multi_dict = request.args
            for key in multi_dict:
                print multi_dict.get(key)
                print "1"
           
            if "addToDo" in request.form:
                functions.insertToDo(user, request.form.get("addToDo"))
                
            if "addHabit" in request.form:
                print "hi"
                print request.form.get("addHabit")
                functions.insertHabit(user, request.form.get("addHabit"))
            if "addGoal" in request.form:
                functions.insertGoal(user, request.form.get("addGoal"))
            if sort == "level":
                lb = functions.getAllUserInfo('level')
            elif sort == "money":
                lb = functions.getAllUserInfo('money')
            elif sort == "events_completed":
                lb = functions.getAllUserInfo('events_completed')
        lb = functions.getAllUserInfo('events_completed')

        #If not a request, load everything
        todos = functions.getUserToDos(user)
        habits = functions.getUserHabits(user)
        goals = functions.getUserGoals(user)
        
        return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb)
    else:
        return redirect(url_for('root'))

@app.route("/authenticate/", methods = ['POST','GET'])
def authenticate():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        hashpass = hashlib.sha224(password).hexdigest()
        if 'login' in request.form:
            if login.login(username,password):
                session['username'] = username
                return redirect(url_for("home",message = "Login successful",sort="level"))
            else:
                return redirect(url_for("home",message = "Login failed",sort="level"))
        else:
            if login.register(username,password):
                return redirect(url_for("home",message = "Registration successful",sort="level"))
            else:
                return redirect(url_for("home",message = "Registration failed",sort="level"))

@app.route("/logout/", methods=['POST','GET'])
def logout():
    session.pop('username')
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    login.initializeTables()
    app.run()
