from flask import Flask
from main.triesDB import initializeDS as db

from main.config import configure_app

app = Flask(__name__, instance_relative_config=True,
            static_folder='./static', template_folder='./templates')

configure_app(app)

# Create an instance of the Tries class and append data
app.data = db.retrieve()

from main import view

