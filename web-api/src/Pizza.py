from bson.json_util import dumps,loads
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pprint import pprint
from src.Messenger import Messenger
import uuid

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['test-database']
collection = db['test-collection']

@app.route("/orders/")
def GetAllOrders():
    all_docs = list(collection.find({}, {'_id': False}))
    print(all_docs)
    return jsonify(all_docs)




order2 = Messenger(address = "Stanevicius", name = "Justinas")
order2.orderRef = 1

@app.route("/orders/<orderRef>", methods=["POST"])
def CreateOne(orderRef):
    order = request.json
    order["orderRef"] = orderRef
    duplicate = collection.find_one({"orderRef": orderRef})

    if(duplicate is not None):
        return jsonify({}), 409

    orderId = collection.insert_one(order).inserted_id
    return jsonify({"orderRef": orderRef}), 201

@app.route("/test/<id>", methods=["POST"])
def AddOne(id):
    order = request.json

    print(order)
    print(id)
    return "testas"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

print("sth default");
print(__name__);

app.run()

###! /usr/bin/python3
###print("Hello, world!")
