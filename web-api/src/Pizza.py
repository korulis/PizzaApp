from flask import Flask, jsonify, request
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

order = {"address": "S. Staneviciaus 14-28", "name": "Justinas"}


@app.route("/")
def GetAll():
    m1 = "This application is called: " + __name__
    m1 = jsonify(order)
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
