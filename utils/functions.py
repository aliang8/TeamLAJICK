import sqlite3 as sql
import hashlib, random

#CONNECT DATABASE                                                                                                       
DATA = "data/data.db"

def getUserID(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT userID FROM accounts WHERE username = ?", (user,))
    userID = data.fetchone()[0]
    return userID

#retrieving all the user information outputted in a tuple
def getUserInfo(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT username, money, level, exp, events_completed, userID FROM accounts WHERE username = ?", (user,))
    stats = data.fetchall()
    return stats[0]

def getAllUserInfo(sort):
    db = sql.connect(DATA)
    c = db.cursor()
    leaderboard = [];
    if sort == "money":
        a = c.execute("SELECT username FROM accounts ORDER BY money DESC")
        users = a.fetchall()
    elif sort == "level":
        a = c.execute("SELECT username FROM accounts ORDER BY level DESC")
        users = a.fetchall()
    elif sort == "events_completed":
        a = c.execute("SELECT username FROM accounts ORDER BY events_completed DESC")
        users = a.fetchall()
    for user in users:
        userInfo = getUserInfo(user[0])
        leaderboard.append(userInfo)
    return leaderboard

def getUserEvents(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ?", (userID,))
    goals = data.fetchall()
    return goals
    
#return the user's goals in a tuple
def getUserToDos(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and todo = 1", (userID,))
    todos = data.fetchall()
    return todos
    
#return the user's goals in a tuple
def getUserHabits(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and habit = 1", (userID,))
    habits = data.fetchall()
    return habits

#return the user's goals in a tuple
def getUserGoals(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and goal = 1", (userID,))
    goals = data.fetchall()
    return goals
    


def insertToDo(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("INSERT INTO events VALUES (?,1,0,0,?)", (userID, goal,))
    
    db.commit()
    db.close()
    return goal

def insertHabit(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("INSERT INTO events VALUES (?,0,1,0,?)", (userID, goal,))
    
    db.commit()
    db.close()
    return goal

#one function for removing and inserting user goals
def insertGoal(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)

    data = c.execute("INSERT INTO events VALUES (?,0,0,1,?)", (userID, goal,))

    db.commit()
    db.close()
    return goal
    
def deleteGoal(user, goalID):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("DELETE FROM events WHERE goalID = ?", goalID)
    
    db.commit()
    db.close()
     
#update and insert user info
def updateInfo(user,infoType,update):
    db = sql.connect(DATA)
    c = db.cursor()
    exists = c.execute("SELECT " + infoType + " from accounts WHERE username = ?", (user,))
    exist = exists.fetchall()
    print len(exist)
    if len(exist) != 0:
        data = c.execute("UPDATE accounts SET " + infoType + " = ? WHERE username = ?", (update, user,))
    else:
        data = c.execute("INSERT INTO accounts (" + infoType + ") VALUES (?) WHERE username = ?", (update,user,)) 
    db.commit()
    db.close()

#edits equipment stats
def updateStats(stats, level, multiplier):
    i = 0
    avg = 0
    for stat in stats:
        stat = int(stat)
        stat = stat * level + multiplier * level
        avg += stat
        stat = str(stat)
        stats[i] = stat
        i += 1
    gold = int(avg/6)
    if gold < 1:
        gold = 1
    gold = str(gold * 5)
    stats.append(gold)
    return stats
    
#makes random equipment for store
def makeEquipment(user):
    level = getUserInfo(user)[3]
    f = open('static/equipment.txt','r')
    equipmentList = f.read().split()[1:]
    n = random.randint(0,len(equipmentList)-1)
    equipment = equipmentList[n].split(',')
    name = equipment[0]
    stats = equipment[1:]
    n = random.randint(1,100)
    if(n >= 1 and n <=80):
        print(0)
        stats = updateStats(stats, level, 0)
    if(n >= 81 and n <=95):
        print(1)
        stats = updateStats(stats, level, 1)
    if(n >= 96 and n <=99):
        print(2)
        stats = updateStats(stats, level, 2)
    elif(n==100):
        print(3)
        stats = updateStats(stats, level, 5)
    equipment[1:] = stats
    return equipment

def makeTR(equipment):
    tr = ""
    price = equipment.pop()
    print(equipment)
    for x in equipment:
        print(x)
        tr += "<td>" + x + "</td>"
    tr += "<td><button id='purchase'>" + price + " Gold</button></td>"
    return tr


