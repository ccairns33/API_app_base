from flask_restful import Resource, request
from flask import jsonify
from app.api.schemas.person_schema import PersonSchema
from marshmallow import ValidationError

names = {
    "carla": {"age": 22, "gender": "female"},
    "bill": {"age": 47, "gender": "male"},
}

person_schema = PersonSchema()

class HelloWorld(Resource):
    # if instance method does not use self, then it can be class method and change self to cls
    
    def post(self, name):
        try:
            data = person_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages,400
        # names[name] is type dict
        return jsonify(data)

    
    def get(self, name):
        return names[name]

# update on app and sends to dashboard
# everytime records have to be updates recieve a ticket on dev team for the item to be displayed on dashboard
# self service add data and shows on dashboard

# store the valid date = null, this is the curretn active items not expires
# valid to in the past would not have to be expired in order to populate those
# request in url 