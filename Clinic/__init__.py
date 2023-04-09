from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/clinic?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db = SQLAlchemy(app=app)


login = LoginManager(app=app)

