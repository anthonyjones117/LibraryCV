#!/usr/bin/env python

from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import requests

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
    

@app.route('/data', methods=['GET'])
def get_data():
    data = list(mycol.find())

    # Convert ObjectId to string for JSON serialization
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data)
    
@app.route('/', methods=['GET'])
def welcome():
    return render_template("./index.html")

@app.route('/books', methods=['GET'])
def search_for_book():
    #data = request.get_json()
    data = 'the lord of the rings'
    OLSearchURL = 'https://openlibrary.org/search.json'
    data_formatted = data.replace(' ', '+')
    book_search = OLSearchURL + '?q=' + data_formatted
        
    res = requests.get(book_search)
    print(res)
    print(jsonify(res))
    print('done')

   # call search openlibrary

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)