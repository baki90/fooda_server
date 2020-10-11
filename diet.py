#about user
from flask_restful import Resource, Api
from flask import request
import db

#food detector
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import yolo.detect as Detector

def nutrient(foodname):
    cursor = db.connect()
    sql = "select * from food where food_name='%s'"%(foodname)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) >0:
        return result
    else:
        return 'fail'

class AnalyzeDiet(Resource):
    def post(self): #if using post method
        value = request.form['token']
        foodImage = request.files['uploaded_file'] #download file from application
        foodImage.save('food.png')
       
        foodname = Detector.foodDetect("../fooda-server/food.png")
        for fn in foodname:
            print(nutrient(fn))
        return {"result": "success"} #return json