from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)

CORS(app)


bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

app.config.from_object(Config)

login = LoginManager(app)



from app import routes
