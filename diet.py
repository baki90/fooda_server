#about user
from flask_restful import Resource, Api
from flask import request
#from yolo import detect as Detector

class AnalyzeDiet(Resource):
    def post(self): #if using post method
        value = request.form['token']
        foodImage = request.files['uploaded_file'] #download file from application
        foodImage.save('food.png')

        #foodname = Detector.foodDetect("../food.png")
        print(foodname)
        return {"result": "success"} #return json