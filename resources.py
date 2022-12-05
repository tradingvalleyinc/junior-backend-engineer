from flask_restful import Resource, reqparse, request
from flask import Response, jsonify
import datetime

from models import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt)
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('name', help = 'This field cannot be blank', required = True)
class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = UserModel(
            username = data['username'],
            password_hash = UserModel.generate_hash(data['password']),
            email = data['email'],
            name = data['name']
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'],expires_delta= datetime.timedelta(seconds=60))
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                }
        except:
            return {'message': 'Something went wrong'}, 500

def printHello(func):
    def wrapper():
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        
        if current_user and UserModel.verify_hash(data['password'], current_user.password_hash) :
            if not request.cookies.get('first') :
                access_token = create_access_token(identity = data['username'],expires_delta= datetime.timedelta(seconds=60))
                
                res = Response('Welcome back, {}!'.format(current_user.username))
                res.set_cookie(key='first', value='1', expires=datetime.datetime.now()+datetime.timedelta(seconds=10))
            
            
                return res
        return func()
    return wrapper
class UserLogin(Resource):
    method_decorators = { 'post': [printHello]}
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if UserModel.verify_hash(data['password'], current_user.password_hash):
            access_token = create_access_token(identity = data['username'],expires_delta= datetime.timedelta(seconds=60))
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                }
            
        else:
            return {'message': 'Wrong credentials'}
      
      

      
      
class AllUsers(Resource):
    @jwt_required()
    def get(self):
        return UserModel.return_all()    