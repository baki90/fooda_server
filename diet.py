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
        return 'fail'

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
        
