#about user
from flask_restful import Resource, Api
from flask import request, jsonify
import db
import weekAnalyze as week
import utils

class AnalyzePerson(Resource):
    def get(self): #if using post method
        email = str(request.args.get('email'))
        userid = utils.userId(email)

        tan, dan, ji = week.weekAnalyze(userid)
        style = week.personType(userid)
        return {"result": "success", "calbohydrate": tan, "protein": dan, "fat": ji, "style": style}