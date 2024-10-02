from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = '16c749724f0c2920edea51b1b4e7af80f9a10f2ed97981830c0c9109f2370862'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FranTrek.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db=SQLAlchemy(app)
app.app_context().push()

from FranTrek import routes