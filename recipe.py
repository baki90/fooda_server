from flask_restful import Resource, Api
from flask import request, jsonify
import foodCrawling as cw


class RecommendRecipe(Resource):
      def get(self): 
        foodname = str(request.args.get('foodname'))
        craw = cw.foodCrawling(foodname)

        return craw