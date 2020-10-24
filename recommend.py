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
        print(userid)
        tan, dan, ji = week.weekAnalyze(userid)
        print(tan)
        print(dan)
        print(ji)
        total = tan +dan + ji
        tanper = 50 - tan/total * 100 
        danper = 30 - dan/total*100
        jiper = 20 - ji/total*100
        return {"result": "success", "carbohydrate": tanper, "protein": danper, "fat": jiper, "tan": tan, "dan": dan, "ji": ji}

class AnalyzeImage(Resource):
    def get(self):
        print('hello')
        print(request.args)
        email = str(request.args.get('email'))
        userid = utils.userId(email)
        tan, dan, ji = week.weekAnalyze(userid)
        img = week.drawGraph(tan,dan,ji)
        return send_file(img, mimetype='image/png')


class AnalyzeTotalDiet(Resource):
    def get(self):
        email = str(request.args.get('email'))
        userid = utils.userId(email)

        conn = db.connect()
        cursor = conn.cursor()
        sql = "SET @DAY := -1;"
        cursor.execute(sql)
        cursor.fetchall()
        sql = "SELECT @DAY := @DAY +1 as DAY, (SELECT COUNT(*) FROM diet WHERE day = @DAY and user_id=%d and date between DATE_ADD(NOW(), INTERVAL -1 WEEK) AND NOW()) as eat FROM diet WHERE @DAY < 3 order by DAY;"%(userid)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        
        style = week.personType(userid)

        res  =  {"mon": result[0]['eat'], "lun": result[1]['eat'], "din": result[2]['eat'], "sna": result[3]['eat'], "style" : style}
        print(res)
        return res

