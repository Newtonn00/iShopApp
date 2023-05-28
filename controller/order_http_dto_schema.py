from marshmallow import Schema, fields
from controller.order_item_http_dto_schema import OrderItemHttpDtoSchema

class OrderHttpDtoSchema(Schema):


    order_id = fields.Integer()
    city = fields.Str()
    status = fields.Integer()
    amount = fields.Float()
    vat_amount = fields.Float()
    weight = fields.Integer()
    created_on = fields.DateTime()
    created_by = fields.Str()
    quantity = fields.Integer()
    customer_no = fields.Str()
    items = fields.List(fields.Nested(OrderItemHttpDtoSchema))