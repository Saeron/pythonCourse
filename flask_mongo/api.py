from flask import Flask, jsonify, request
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["usersdb"]
users = db["users"]

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def get_db():
    lista = list()
    list_names = users.find()
    for i in list_names:
        name = i.get("name")
        email = i.get("email")
        lista.append({"name": name, "email":email})
    return jsonify(lista)

@app.route('/put', methods=['GET'])
def put_some():
   users.insert({"name": "Saeron","email": "antdcs@gmail.com"})
   return "<h1>User added.</h1"



app.run()
