from flask_restful import Resource
from flask import jsonify

names = {
        "carla": {"age":22, "gender": "female"},
        "bill": {"age": 47, "gender": "male"}
        }

class HelloWorld(Resource):
    def get(self, name):
        # names[name] is type dict
        return jsonify(names[name])

    def post(self, name):
        return {"data": " Posted"}