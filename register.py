#about user
from flask_restful import Resource, Api
from flask import request
import utils
import db

class Register(Resource):
    def post(self): #if using post method
        email = str(request.form['email'])
        password = str(request.form['password'])
        name = str(request.form['name'])
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        sex = request.form['sex']

        if utils.isUser(email):
            return {"result": "fail", "msg": "이미 존재하는 아이디입니다."} 
        else:
            cursor =db.connect()
            sql = "insert into user values ('%s', '%s', %d, %f, %f, '%c', 0, 0, '%s')"%(email, name,age,height,weight,sex, password)
            print(sql)
            cursor.execute(sql)
            db.conn.commit()
            return {"result": "success", "msg": "회원가입이 완료되었습니다.", "token": 'token'} 

        