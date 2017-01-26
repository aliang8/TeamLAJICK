#import flask
import os
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
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

        stats = [50,0,0,0,0,0]
    
        for item in inventory:
            stats[0] += item[3]
            stats[1] += item[4]
            stats[2] += item[5]
            stats[3] += item[6]
            stats[4] += item[7]
            stats[5] += item[8]

        width_health = ((float(userInfo[5]) / stats[0]) * 100)
        width_exp = ((float(userInfo[3]) / 150) * 100)
        userInfo = userInfo + (width_health,width_exp,)
        #Check for all ajax requests here
        #All of POST type
        gold = functions.getUserInfo(user)[1]
        if request.method == 'POST':

             return   

        lbM = functions.getAllUserInfo('money')
        lbL = functions.getAllUserInfo('level')
        lbE = functions.getAllUserInfo('events_completed')
        
        return render_template('dashboard.html', logged = 1, message=message,todos=todos, habits=habits, goals=goals, balance=gold, userInfo=userInfo, lbL=lbL, lbM=lbM, lbE=lbE, equipments=equipments, inventory=inventory, stats=stats)
    else:
        lbM = functions.getAllUserInfo('money')
        lbL = functions.getAllUserInfo('level')
        lbE = functions.getAllUserInfo('events_completed')
        return render_template('dashboard.html', logged = 0, lbL=lbL, lbM=lbM, lbE=lbE)


@app.route("/newtodo", methods=['POST'])
def newtodo():
    user = session.get('username')
    a,b = functions.insertToDo(user, request.form.get("addToDo"))
    return jsonify(id=a, task=b)
    
@app.route("/newhabit", methods=['POST'])
def newhabit():
    user = session.get('username')
    a,b = functions.insertHabit(user, request.form.get("addHabit"))
    return jsonify(id=a, task=b)
    
@app.route("/newgoal", methods=['POST'])
def newgoal():
    user = session.get('username')
    a,b =  functions.insertGoal(user, request.form.get("addGoal"))
    return jsonify(id=a, task=b)
    
@app.route("/buy", methods=['POST'])
def buy():
    user = session.get('username')
    price = request.form.get("price")
    price = int(price)
    return functions.buyItem(user, price)
    
@app.route("/complete", methods=['POST'])
def complete():
    user = session.get('username')
    level,exp = functions.exp(user, 20)
    return jsonify(level=level, exp=exp)



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
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    login.initializeTables()
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
