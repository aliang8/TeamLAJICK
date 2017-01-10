import sqlite3 as sql
import hashlib

#CONNECT DATABASE                                                                                                       
DATA = "../data/data.db"

#retrieving all the user information outputted in a tuple
def getUserInfo(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT money, level, exp FROM accounts WHERE username = ?", (user,))
    stats = data.fetchall()
    return stats[0]

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


