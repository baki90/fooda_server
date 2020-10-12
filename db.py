import pymysql



def connect():
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='foodai',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

    return conn

def close(conn):
    conn.close()

def userinfo(id):
    cursor = connect().cursor()
    sql = "SELECT * FROM foodai WHERE id = '%s'"%(id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        return 

