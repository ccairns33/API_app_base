from marshmallow import Schema, fields

class PersonSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)