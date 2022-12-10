from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

def setUpDB(app):
    # global db

    host=os.environ.get('postgre_host')
    database=os.environ.get('postgre_database')
    user=os.environ.get('postgre_user')
    password=os.environ.get('postgre_password')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    db.init_app(app)

    class UserTable(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique=True, nullable=False)
        password = db.Column(db.String, nullable=False)
        realname = db.Column(db.String, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False)
    with app.app_context():
        db.create_all()
    return UserTable

def addUser(app, user):
    with app.app_context():
        db.session.add(user)
        db.session.commit()