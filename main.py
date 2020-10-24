from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import json


#import using file (users.py 파일의 Users class)
from diet import AnalyzeDiet, UploadDiet, TotalDiet,TotalDietList
from login import Login
from register import Register
from user import User, UserHcal
from recommend import AnalyzePerson, AnalyzeImage, AnalyzeTotalDiet
from board import GetPostByBoardId
from recipe import RecommendRecipe

app = Flask(__name__)
CORS(app)

@app.route('/')
def Fooda():
    return "Im Fooda!"

if __name__ == '__main__':
    api = Api(app)
    #Users : Class name, /users: Resource url
    #앞으로 resource 추가할 때, 아래와 같이 추가하면 됨!
    api.add_resource(AnalyzeDiet, '/analyzeDiet')
    api.add_resource(UploadDiet, '/uploadDiet')
    api.add_resource(TotalDiet, '/totalDiet')
    api.add_resource(TotalDietList, '/totalDietList')
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(User, '/user')
    api.add_resource(UserHcal, '/userHcal')
    api.add_resource(AnalyzePerson, '/analyzePerson')
    api.add_resource(AnalyzeImage, '/analyzeImage')
    api.add_resource(AnalyzeTotalDiet, '/analyzeTotalDiet')

    api.add_resource(RecommendRecipe, '/recipe')
    api.add_resource(GetPostByBoardId, '/getPostbyboardid')




    port = os.getenv('PORT', 3000)
    app.run(host='0.0.0.0', port = port)
