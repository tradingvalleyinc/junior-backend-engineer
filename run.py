from flask import Flask, session
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from flask_session import Session
app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'test'
jwt = JWTManager(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@mysql-server:3306/mysql"
app.config['SECRET_KEY'] = 'my_precious'
db = SQLAlchemy(app)
@app.before_first_request
def create_tables():
    db.create_all()
import views, models, resources

api.add_resource(resources.UserRegistration, '/user')
api.add_resource(resources.UserLogin, '/user/login')
api.add_resource(resources.AllUsers, '/user')