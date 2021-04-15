import os

from flask import Flask, jsonify, request

products = [
    {'id': '1',
     'name': 'zzz',
     'description': 'this is product 1',
     'price': 'USD',
     'quantity': '10'
     },
    {'id': '2',
     'name': 'abc',
     'description': 'this is product 2',
     'price': 'USD',
     'quantity': '20'
     }

]

app = Flask(__name__)


@app.route('/')
def index():
    return "hello this is a response"


# get all the courses
@app.route("/products/", methods=['GET'])
def get():
    return jsonify(products)


# get course by id
@app.route("/products/<int:id>", methods=['GET'])
def get_product(id):
    print(products.__getitem__(id))
    return jsonify(id)


if __name__ == "__main__":
    app.run(debug=True)
