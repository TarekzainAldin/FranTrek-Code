import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask_mail import Mail
from FranTrek.config import config
app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ckeditor = CKEditor(app)
modal = Modal(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


mail = Mail(app)
from FranTrek.main.routes import main 
from FranTrek.users.routes import users
from FranTrek.lessons.routes import lessons
from FranTrek.courses.routes import courses_bp

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(lessons)
app.register_blueprint(courses_bp)
