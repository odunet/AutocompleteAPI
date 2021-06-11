# import module
from dotenv import load_dotenv
from flask import Flask, url_for, render_template, redirect, request, jsonify
import os
from main import application
# from main.triesDS import Tries
# from main.triesData import data

# Enable CORS
from flask_cors import CORS, cross_origin
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

# load environment variables into module
load_dotenv()

# get secret key from environment
application.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@application.route('/', methods=["GET"])
@cross_origin()
def index():
    return render_template('index.html')


@application.route('/api/<key>', methods=["GET"])
@cross_origin()
def search(key):
    """
        Parameters
        ----------
        key : str
            A key are arguments send with the url "GET" request from the client.

        Request Type
        -------
        methods = GET


        Returns
        -------
        list
            The list contains strings of predicted autocomplete items e.g.:
            ['oluwatosin', 'oluwaseun', 'oluwasegun', 'oluwakemi', 'olumide', 'olufunso',
            'olufemi', 'oluremi', 'olushola']
    """
    if not key:
        return "No key included"
    else:
        # perform auto search on the instance of Tries
        result = application.data.autoSearch(key)

        # Handle result of search and send to server.
        if result[0] == False:
            print({'Error': 'No Result Found'})
            return jsonify([])
        else:
            jsonData = []
            for index, i in enumerate((result[1])):
                jsonData.append(i)
            return jsonify(jsonData)
