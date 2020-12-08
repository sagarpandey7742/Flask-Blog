from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '2ade7dca04722e1dc2aa38dd6c31023898993cf0291432e811cee85e3526e898'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

from app import routes
