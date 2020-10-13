#about user
from flask_restful import Resource, Api
from flask import request, jsonify, send_file
import db
import weekAnalyze as week
import utils

class AnalyzePerson(Resource):
    def get(self): 
        email = str(request.args.get('email'))
        userid = utils.userId(email)

        tan, dan, ji = week.weekAnalyze(userid)
        style = week.personType(userid)
        return {"result": "success", "carbohydrate": tan, "protein": dan, "fat": ji, "style": style}

class AnalyzeImage(Resource):
    def get(self):
        print('hello')
        print(request.args)
        email = str(request.args.get('email'))
        userid = utils.userId(email)
        tan, dan, ji = week.weekAnalyze(userid)
        img = week.drawGraph(tan,dan,ji)
        return send_file(img, mimetype='image/png')

