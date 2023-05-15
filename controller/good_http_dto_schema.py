from marshmallow import Schema, fields

class GoodHttpDtoSchema(Schema):
    good_id = fields.Integer()
    name = fields.Str()
    category = fields.Str()
    availqty = fields.Integer()
    status = fields.Integer()