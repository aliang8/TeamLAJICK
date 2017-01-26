import sqlite3 as sql
import hashlib

#CONNECT DATABASE
DATA = "data/data.db"

#Initialize databases. Only works once.
def initializeTables():
    db = sql.connect(DATA)
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS accounts (username TEXT NOT NULL, password TEXT NOT NULL, money INTEGER, level INTEGER, exp INTEGER, events_completed INTEGER, hp INTEGER, userID INTEGER PRIMARY KEY autoincrement)")
    c.execute("CREATE TABLE IF NOT EXISTS events (goalID INTEGER PRIMARY KEY autoincrement, userID INTEGER, todo INTEGER, habit INTEGER, goal INTEGER, content TEXT NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS inventory (userID INTEGER, item TEXT NOT NULL, hp INTEGER, atk INTEGER, atkspeed INTEGER, speed INTEGER, def INTEGER, int INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS shop (userID INTEGER, item TEXT NOT NULL, hp INTEGER, atk INTEGER, atkspeed INTEGER, speed INTEGER, def INTEGER, int INTEGER, shop INTEGER)")
    db.commit()
    db.close()
    
def register(username, password):
    hashpass = hashlib.sha224(password).hexdigest()
    creds = (username,hashpass,500,1,0,0,50)
    db = sql.connect(DATA)
    c = db.cursor()
    users = c.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    if len(c.fetchall()) == 0 and len(password) >= 3:
        c.execute("INSERT INTO accounts (username,password,money,level,exp,events_completed,hp) VALUES (?,?,?,?,?,?)", creds)
        db.commit()
        return True
    else:
        return False
    
def login(username,password):
    hashpass = hashlib.sha224(password).hexdigest()
    db = sql.connect(DATA)
    c = db.cursor()
    users = c.execute("SELECT password FROM accounts WHERE username = ?", (username,))
    data = users.fetchall()
    if len(data) == 0:
        return False
    elif data[0][0] == hashpass:
        return True
    db.commit()

def changePass(username,oldpass,newpass):
    hashnewpass = hashlib.sha224(newpass).hexdigest()
    db = sql.connect(DATA)
    c = db.cursor()
    exists = login(username,oldpass)
    if exists:
        c.execute("UPDATE accounts SET password = ? WHERE username = ?", (hashnewpass,username,))
        db.commit()
        return True
    else:
        return False
