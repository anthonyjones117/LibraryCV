#!/usr/bin/env python

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
DATABASE_NAME = "mydatabase"
COLLECTION_NAME = "customers"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
mycol = db[COLLECTION_NAME]

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)

@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    if data:
        result = mycol.insert_one(data)
        return jsonify({'message': 'Data added successfully', 'inserted_id': str(result.inserted_id)}), 201
    else:
        return jsonify({'message': 'No data provided'}), 400
    
@app.route('/', methods=['GET'])
def welcome():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)