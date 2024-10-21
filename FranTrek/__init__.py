from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
app = Flask(__name__)

app.config[
    "SECRET_KEY"
] = '16c749724f0c2920edea51b1b4e7af80f9a10f2ed97981830c0c9109f2370862'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FranTrek.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ckeditor = CKEditor(app)
modal = Modal(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from FranTrek import routes