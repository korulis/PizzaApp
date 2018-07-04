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
    all_docs = [remove_key(x, "_id") for x in list(collection.find())]
    all_docs = list(collection.find({}, {'_id': False}))
    print(all_docs)
    print(len(all_docs))
    serialized = dumps(all_docs)
    aaa = loads(serialized)
    lstmano = list(aaa)
    print(lstmano)
    #uzu = jsonify(lstmano)
    #return jsonify({"afds":"sadfas"})
    return jsonify(all_docs)



def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r

order = {"address": "S. Staneviciaus 14-28", "name": "Justinas"}
order2 = Messenger(address = "Stanevicius", name = "Justinas")
order2.orderRef = 1

@app.route("/")
def GetAll():
    print("starter")
    m1 = "This application is called: " + __name__
    #    m1 = jsonify(order)

    print("afds")
    jj = dumps(order2.getDict())
    print(jj)
    print("afdsdsa")

    orderId = collection.insert_one(order2.getDict()).inserted_id
    db.collection_names(include_system_collections=False)
    #    my_collections = db.collection_names(include_system_collections=False)
    first_doc = list(collection.find())
    serialized = dumps(first_doc)
    #pprint(first_doc)
    print(serialized)
    m1 = "This application is called: " + "   "
    return m1

@app.route("/test/<id>", methods=["POST"])
def AddOne(id):
    content = request.json
    print(content)
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
