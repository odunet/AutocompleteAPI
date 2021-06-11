from flask import Flask
from main.datastore import db as triesDB

from main.config import configure_app

app = Flask(__name__, instance_relative_config=True,
            static_folder='./static', template_folder='./templates')

configure_app(app)

# Create an instance of the Tries class and append data
app.data = triesDB.retrieve()

from main import view

