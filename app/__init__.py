from flask import Flask
from app.config import BaseConfig
#from app.database import db


# initialize Flask
app = Flask(__name__)

# load configuration file
app.config.from_object(BaseConfig)

# initialize database
#db.init_app(app)

from app import database
from app import routes

if __name__ == '__main__':
    # use_debugger(browser-based debugger), passthrough_errors option is the key to make crashes reach the PyCharm
    app.run(debug=True)
