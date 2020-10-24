#about user
from flask_restful import Resource, Api
from flask import request, jsonify
import db
import utils

#food detector
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import yolo.detect as Detector


def nutrient(foodname):
        
    conn = db.connect()
    cursor = conn.cursor()

    sql = "select food_id, korean as food_name, calories, carbohydrate, protein, fat, gram from food where food_name='%s'"%(foodname)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close(conn)
    if len(result) >0:
        return result[0]
    else:
        return 'false'

class AnalyzeDiet(Resource):
    def post(self): #if using post method
        print("hello")
        value = request.form['token']
        foodImage = request.files['uploaded_file'] #download file from application
        foodImage.save('food.png')
       
        foodname = Detector.foodDetect("../fooda-server/food.png")
        print(nutrient(foodname[0]))
        return nutrient(foodname[0]) #return json


class UploadDiet(Resource):
    def post(self):
        foodid = request.form['food_id']
        email = str(request.form['email'])
        day = request.form['day']
        print(email)
        userid = utils.userId(email)
        print(userid)    
        conn = db.connect() 
        cursor = conn.cursor()
        sql = "insert into diet(user_id, date, day, food_id) values(%d, NOW(), %d, %d)"%(int(userid), int(day), int(foodid))
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)

        return {"result" : "success"}
        
#날짜, 유저에 대한 하루 총 칼로리량 반환
class TotalDiet(Resource):
    def get(self):
        email = str(request.args.get('email'))
        date = request.args.get('datetime')
        
        conn = db.connect()
        cursor = conn.cursor()
        
        userid = utils.userId(email)
        kicho = utils.userhcal(email)
        #해당 날짜의 섭취한 음식을 모두 빼내고
        sql = "select * from diet where user_id = %d and DATE(date)='%s'"%(userid, date)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        kcal = 0
        tan =0
        dan =0
        ji = 0

        if len(result) >0:
            for res in result:
                food_id = int(res['food_id'])
                sql = "select * from food where food_id = %d"%(food_id)
                cursor.execute(sql)
                out = cursor.fetchall()[0]
                kcal += out['calories']
                tan += out['carbohydrate']
                dan += out['protein']
                ji += out['fat']
            db.close(conn)
            return {"result" : "success", "calories" : kcal, "carbohydrate":tan, "protein":dan, "fat": ji, "kicho" : kicho}

        else:
            db.close(conn)
            return {"result":"fail"}

class TotalDietList(Resource):
     def get(self):
        email = str(request.args.get('email'))
        date = request.args.get('datetime')
        userid = utils.userId(email)
        print(userid)
        
        conn = db.connect()
        cursor = conn.cursor()
        sql = "select d.day as day, f.korean as food_name, f.calories as cal, f.gram as gram from diet as d JOIN food as f on d.food_id = f.food_id where user_id= %d and DATE(date)='%s' ORDER BY day "%(userid, date)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        return result
