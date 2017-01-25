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
    return render_template('dashboard.html', login = 0)
    
@app.route("/<message>", methods=['POST','GET'])
def home(message):
    print session.get('username');
    if session.get('username') != None:
        user = session.get('username')
        userInfo = functions.getUserInfo(user)

        return render_template('dashboard.html', message=message, userInfo=userInfo)
    '''
    if session.get('username'):
        user = session.get('username')
    
        #Check for all ajax requests here
        #All of POST type
        if request.method == 'POST':
            if "addToDo" in request.form:
                return functions.insertToDo(user, request.form.get("addToDo"))
            if "addHabit" in request.form:
                return functions.insertHabit(user, request.form.get("addHabit"))
            if "addGoal" in request.form:
                return functions.insertGoal(user, request.form.get("addGoal"))
            return 
            
    
    
        #If not a request, load everything
        todos = functions.getUserToDos(user)
        habits = functions.getUserHabits(user)
        goals = functions.getUserGoals(user)
        
        return render_template('dashboard.html', todos=todos, habits=habits, goals=goals, message=message)
    '''

    
    return render_template('dashboard.html', message=message)


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
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
