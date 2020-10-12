#about user
from flask_restful import Resource, Api
from flask import request, jsonify
import db

#사용자의 주간 섭취율을 탄, 단, 지 순으로 반환함
def weekAnalyze(userid):
    conn = db.connect()
    cursor = conn.cursor()
    sql = "select SUM(f.carbohydrate) as car, SUM(f.protein) as pro, SUM(f.fat) as fat from diet as d JOIN food as f on d.food_id = f.food_id where user_id=%d and d.date between DATE_ADD(NOW(), INTERVAL -1 WEEK) AND NOW();"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    db.close(conn)
    return result['car'], result['pro'], result['fat']

class analyzePerson(Resource):
    def post(self): #if using post method
        email = str(request.args.get('email'))

        conn = db.connect()
        cursor = conn.cursor()
        sql = "select d.day as day, f.korean as food_name, f.calories as cal, f.gram as gram from diet as d JOIN food as f on d.food_id = f.food_id where user_id= %d and DATE(date)='%s' ORDER BY day "%(userid, date)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)