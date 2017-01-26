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
    
@app.route("/<message>/<sort>", methods=['POST','GET'])
def home(message,sort):
    if session.get('username') != None:
        user = session.get('username')
        userInfo = functions.getUserInfo(user)
        #If not a request, load everything
        todos = functions.getUserToDos(user)
        habits = functions.getUserHabits(user)
        goals = functions.getUserGoals(user)

        #Check for all ajax requests here
        #All of POST type
        gold = functions.getUserInfo(user)[1]
        equipment1 = functions.makeTR(makeEquipment(user))
        equipment2 = functions.makeTR(makeEquipment(user))
        equipment3 = functions.makeTR(makeEquipment(user))
        if request.method == 'POST':
            multi_dict = request.args
            for key in multi_dict:
                print multi_dict.get(key)
                print "1"
           
            if "addToDo" in request.form:
                print request.form.get("addToDo")
                return functions.insertToDo(user, request.form.get("addToDo"))
            if "addHabit" in request.form:
                return functions.insertHabit(user, request.form.get("addHabit"))
            if "addGoal" in request.form:
                return functions.insertGoal(user, request.form.get("addGoal"))
            if sort == "level":
                lb = functions.getAllUserInfo('level')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipment1 = equipment1, equipment2 = equipment2, equipment3 = equipment3)
            elif sort == "money":
                lb = functions.getAllUserInfo('money')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipment1 = equipment1, equipment2 = equipment2, equipment3 = equipment3)
            elif sort == "events_completed":
                lb = functions.getAllUserInfo('events_completed')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipment1 = equipment1, equipment2 = equipment2, equipment3 = equipment3)
            else:
                lb = functions.getAllUserInfo('events_completed')
        
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
