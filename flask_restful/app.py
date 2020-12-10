from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'store_no_1',
        'items': [
            {
                'name': 'item no 1',
                'pric': 3.365
            }


        ]
    },
    {
        'name': 'store_no_2',
        'items': [
            {
                'name': 'shoe',
                'pric': 63.2
            }


        ]
    }
]

# POST - /store data


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': [
        ]
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET - /store


@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

# GET - /store/name


@app.route('/store/<string:name>/')
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['name'])
        else:
            return jsonify({'message': 'store not found'})


# POST - store items
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_store(name):
    requst_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': requst_data['name'],
                'price': requst_data['price']}
            store['items'].append(new_item)

            return jsonify(store)
        else:
            return jsonify({'message': 'error not found'})


#GET - store/name/items
@app.route('/store/<string:name>/items')
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)
