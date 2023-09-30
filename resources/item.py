import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError
# Here exc is exception, SQLAlchemyError includes all errors captured by SQLAlchemy

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted!"}
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    # Order matters - make sure to put response decorator after the argument decorator
    def put(self, item_data, item_id):
        # Here arg decorator param 'item_data' goes before root arg 'item_id'
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found!")

@blp.route("/item/")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # Note now this is returning list of items instead of object with items
        # This may impact how client receives it, but tradeoff is simpler validation
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            # This will add to db table
            db.session.commit()
            # commit all the transaction
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item!")
        
        return item
