#about user
from flask_restful import Resource, Api
from flask import request
import utils
import db

class User(Resource):
    def get(self): #if using post method
        email = str(request.args.get('email'))
        cursor = db.connect()
        sql = "select * from user where = '%s'"%(email)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) >0:
            return result
        else: return {'result' :'fail'}

class userHcal(Resource):
    def get(self):
        email = str(requset.args.get('email'))

        sql = "SELECT * FROM user WHERE email='%s'"%(userid)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0:
            if result[0]['sex'] =='F':
                age = result[0]['age']
                key = result[0]['height']
                mom = result[0]['weight']
                kicho = 655.1+9.56*mom+1.85*key-4.68*age
                return kicho
            else:
                age = result[0]['age']
                key = result[0]['height']
                mom = result[0]['weight']
                kicho = 66.41+13.75*mom+5*key-6.76*age
                return kicho

        else: return {"result": "fail"}

