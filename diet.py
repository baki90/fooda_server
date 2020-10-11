#about user
from flask_restful import Resource, Api
from flask import request
import db
import utils

#food detector
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import yolo.detect as Detector

cursor = db.connect()

def nutrient(foodname):
    sql = "select food_id, korean as food_name, calories, carbohydrate, protein, fat, gram from food where food_name='%s'"%(foodname)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) >0:
        return result[0]
    else:
        return 'false'

class AnalyzeDiet(Resource):
    def post(self): #if using post method
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

        userid = utils.userId(email)

        sql = "insert into diet(user_id, date, day, food_id) values(%d, NOW(), %d, %d)"%(int(userid), int(day), int(foodid))
        print(sql)
        cursor.execute(sql)
        db.conn.commit()

        return {"result" : "success"}
        
#날짜, 유저에 대한 하루 총 식사량 반환
class totalDiet(Resorce):
    def get(self):
        email = str(request.args.get('email'))
        date = request.args.get('datetime')

        #해당 날짜의 섭취한 음식을 모두 빼내고
        sql = "select * from diet where id = '%s' and DATE(date)='%s'"%(email, date)
        cursor.execute(sql)
        result = cursor.fetchall()
        kcal = 0
        tan =0
        dan =0
        ji = 0
        if len(result) >0:
            for res in result:
                food_id = int(['food_id'])
                sql = "select * from food where food_id = %d"%(food_id)
                cursor.execute(sql)
                out = cursor.fetchall()
                kcal += out['calories']
                tan += out['carbohydrate']
                dan += out['protein']
                ji += out['fat']
            

        else:
            return {"result":"fail"}

