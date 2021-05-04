# import module
from dotenv import load_dotenv
from flask import Flask, url_for, render_template, redirect, request, jsonify
import os
from main import app
from main.triesDS import Tries
from main.triesData import data

# Enable CORS
from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# load environment variables into module
load_dotenv()

# get secret key from environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=["GET"])
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/api/<key>', methods=["POST", "GET"])
@cross_origin()
def searchB(key):
    if not key:
        return "No key included"
    else:
        testTrie = Tries()
        for i in range(len(data)):
            testTrie[data[i]] = data[i]
        result = testTrie.autoSearch(key)
        if result[0] == False:
            print({'Error': 'No Result Found'})
            return jsonify([])
        else:
            jsonData = []
            for index, i in enumerate((result[1])):
                jsonData.append(i)
            return jsonify(jsonData)

# @app.route('/api/<key>', methods=["POST", "GET"])
# def searchA(key):
#     if not key:
#         return "No key included"
#     else:
#         testTrie = Tries()
#         for i in range(len(data)):
#             testTrie[data[i]] = data[i]
#         return str(testTrie.autoSearch(key))
