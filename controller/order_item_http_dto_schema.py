from marshmallow import Schema, fields


class OrderItemHttpDtoSchema(Schema):
    order_id = fields.Integer()
    item_no = fields.Integer()
    good_id = fields.Integer()
    good_name = fields.Str()
    quantity = fields.Integer()