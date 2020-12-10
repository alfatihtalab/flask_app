from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identety, users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)

jwt = JWT(app, authenticate, identety)  # /auth
items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'item not found'}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'an item with name {} already exists !'.format(name)}, 400
        data = request.get_json()
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)
        return new_item, 201

    def delete(self, name):
        global items
        items = filter(lambda x: x['name'] != name, items)
        return {"message ": "item with name {} deleted ".format(name)}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help='this is rquired '
        )
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
