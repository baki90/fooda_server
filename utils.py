import db
from passlib.hash import sha256_crypt

cursor = db.connect()
def isUser(userid):
    sql = "SELECT * FROM user WHERE email='%s'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) >0:
        return True
    else: return False

def userLogin(userid, password):
    sql = "SELECT * FROM user WHERE email='%s'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) >0:
        if (password == result[0]['password']):
            return True
        else: return False
    else: return False