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

@app.route("/orders/<orderRef>", methods=["POST"])
def CreateOne(orderRef):
    order = request.json
    order["orderRef"] = orderRef
    duplicate = collection.find_one({"orderRef": orderRef})

    if(duplicate is not None):
        return jsonify({}), 409

    orderId = collection.insert_one(order).inserted_id
    return jsonify({"orderRef": orderRef}), 201

@app.route("/orders/<orderRef>", methods=["DELETE"])
def RemoveOne(orderRef):
    target = collection.find_one({"orderRef": orderRef})

    if(target is None):
        return jsonify({}), 404

    collection.delete_one({"orderRef": orderRef})
    return jsonify({"orderRef": orderRef}), 202


app.run()

