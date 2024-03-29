from flask_marshmallow import Marshmallow
from marshmallow import EXCLUDE
from app.api.models.person_model import PersonModel

ma = Marshmallow()

class PersonSchema(ma.Schema):
    class Meta:
        # must have fields labeled or will result in Unknown Field errors
        # no need to add id field, will be added automatically
        fields = ("name", "age", "gender", "email" )
        model = PersonModel
        # load_only = ("email",)
    
   