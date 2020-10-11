import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='foodai',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)


def connect():
    return conn.cursor()

def userinfo(id):
    cursor = connect()
    sql = "SELECT * FROM foodai WHERE id = '%s'"%(id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        return 

