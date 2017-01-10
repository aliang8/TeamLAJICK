import sqlite3 as sql
import hashlib

#CONNECT DATABASE                                                                                                       
DATA = "../data/data.db"

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
    data = c.execute("SELECT money, level, exp FROM accounts WHERE username = ?", (user,))
    stats = data.fetchall()
    return stats[0]

#return the user's goals in a tuple
def getUserGoals(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ?", (userID,))
    goals = data.fetchall()
    return goals

#one function for removing and inserting user goals
def goalie(user, goal, method):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    if method == "insert":
        data = c.execute("INSERT INTO events VALUES (?,?)", (userID, goal,))
    elif method == "delete":
        data = c.execute("DELETE FROM events WHERE userID = ? AND goal = ?", (userID, goal,)) 
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


updateInfo('j','money','4')
goalie('j','do hwk','insert')
print getUserGoals('j')
