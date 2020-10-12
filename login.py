#about user
from flask_restful import Resource, Api
from flask import request
import utils

class Login(Resource):
    def post(self): #if using post method
        email = str(request.form['email'])
        password = request.form['password']
        
        if utils.isUser(email):
            if utils.userLogin(email, password):
                print('hello')
                return {"result": "success", "msg": "로그인에 성공했습니다.", "token": email} 
            else:
                return {"result": "fail", "msg": "비밀번호가 틀렸습니다."} 
        else :
            return {"result": "fail", "msg": "아이디가 존재하지 않습니다."} 
        