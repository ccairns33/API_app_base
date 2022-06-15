from flask_restful import Resource, request
from flask import jsonify, current_app
from app.api.schemas.person_schema import PersonSchema
from marshmallow import ValidationError
from app.api.models.person_model import PersonModel
# solves circular import...
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

 
names = {
    "carla": {"age": 22, "gender": "female"},
    "bill": {"age": 47, "gender": "male"},
}

person_schema = PersonSchema()

class HelloWorld(Resource):
    # if instance method does not use self, then it can be class method and change self to cls
    
    def post(self, name):
        posted_data = request.get_json()
        try:
            # make sure there are no validation errors
            # with Marshmallow and model, the .load(posted data) creates and data object of person 
            person_dict = person_schema.load(posted_data)
        except ValidationError as err:
            return f"Errors: {err.messages}",400
        print(person_dict)
        # must pass in PersonModel for Self. not sure why.
        if PersonModel.find_by_email(PersonModel,email=person_dict["email"]):
            return {"message": "Person is already here."}, 400

        person = PersonModel(**person_dict)
        person.save_to_db()

        return {"message": "Person added to the database"}, 201
            
    def get(self, name):
        return names[name]

# update on app and sends to dashboard
# everytime records have to be updates recieve a ticket on dev team for the item to be displayed on dashboard
# self service add data and shows on dashboard

# store the valid date = null, this is the curretn active items not expires
# valid to in the past would not have to be expired in order to populate those
# request in url 