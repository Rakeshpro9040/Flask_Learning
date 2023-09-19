from marshmallow import Schema, fields

#  This is for item create
class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

# This is for store create
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class StoreUpdateSchema(Schema):
    name = fields.Str()
