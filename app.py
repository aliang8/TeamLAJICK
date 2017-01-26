#import flask
import os
from flask import Flask, render_template, session, redirect, url_for, request
from utils import functions, login
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'life^2'
    
@app.route("/", methods=['POST','GET'])
def home():
    message = ""
    
    if session.get('username') != None:
        user = session.get('username')
        userInfo = functions.getUserInfo(user)

        #If not a request, load everything
        todos = functions.getUserToDos(user)
        habits = functions.getUserHabits(user)
        goals = functions.getUserGoals(user)
        equipments = functions.makeShop(user)
        inventory = functions.getUserInventory(user)
        #Check for all ajax requests here
        #All of POST type
        gold = functions.getUserInfo(user)[1]
        if request.method == 'POST':
             return   
        '''
            if sort == "level":
                lb = functions.getAllUserInfo('level')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipments = equipments)
            elif sort == "money":
                lb = functions.getAllUserInfo('money')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipments = equipments)
            elif sort == "events_completed":
                lb = functions.getAllUserInfo('events_completed')
                return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipments = equipments)
        else:
            lb = functions.getAllUserInfo('events_completed')
        '''
        lb = functions.getAllUserInfo('events_completed')
        
        return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lb=lb, equipments = equipments, inventory = inventory)
    else:
        lb = functions.getAllUserInfo('events_completed')
        return render_template('dashboard.html', logged = 0, lb=lb)


@app.route("/newtodo", methods=['POST'])
def newtodo():
    user = session.get('username')
    return functions.insertToDo(user, request.form.get("addToDo"))
    
@app.route("/newhabit", methods=['POST'])
def newhabit():
    user = session.get('username')
    return functions.insertHabit(user, request.form.get("addHabit"))

@app.route("/newgoal", methods=['POST'])
def newgoal():
    user = session.get('username')
    return functions.insertGoal(user, request.form.get("addGoal"))
    
@app.route("/buy", methods=['POST'])
def buy():
    user = session.get('username')
    price = request.form.get("price")
    return functions.buyItem(user, price)

    
    

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
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
