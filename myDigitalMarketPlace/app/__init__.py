from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
 
flaskObj = Flask(__name__)

flaskObj.config.from_mapping(SECRET_KEY = '3XP4sF86N.t\$eSa', SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'))

db = SQLAlchemy(flaskObj)

login_manager = LoginManager(flaskObj)
login_manager.login_view = 'login'


