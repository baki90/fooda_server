import db
from passlib.hash import sha256_crypt

def isUser(userid):
    conn = db.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM user WHERE email='%s'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close(conn)
    if len(result) >0:
        return True
    else: return False

def userLogin(userid, password):
    conn = db.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM user WHERE email='%s'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close(conn)
    if len(result) >0:
        if (password == result[0]['password']):
            return True
        else: return False
    else: return False

def userId(userid):
    conn = db.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM user WHERE email='%s'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close(conn)
    if len(result) >0:
        return result[0]['id']
    else: return False

def userhcal(email):
    conn = db.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM user WHERE email='%s'"%(email)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close(conn)
    if len(result) > 0:
        if result[0]['sex'] =='F':
            age = result[0]['age']
            key = result[0]['height']
            mom = result[0]['weight']
            kicho = 655.1+9.56*mom+1.85*key-4.68*age
            return kicho
        else:
            age = result[0]['age']
            key = result[0]['height']
            mom = result[0]['weight']
            kicho = 66.41+13.75*mom+5*key-6.76*age
            return kicho
