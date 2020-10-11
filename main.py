from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import json


#import using file (users.py 파일의 Users class)
from diet import AnalyzeDiet
from user import Login
from register import Register

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
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')

    port = os.getenv('PORT', 3000)
    app.run(host='0.0.0.0', port = port)
