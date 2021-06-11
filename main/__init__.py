from flask import Flask
from main.triesDB import initializeDS as db

from main.config import configure_app

application = Flask(__name__, instance_relative_config=True,
            static_folder='./static', template_folder='./templates')

configure_app(application)

# Create an instance of the Tries class and append data
application.data = db.retrieve()

from main import view

