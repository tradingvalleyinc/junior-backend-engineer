from flask import Flask, request
from package.sqlalchemy_config import setUpDB, addUser
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)
import datetime
from flask import jsonify
import json

app = Flask(__name__)
 
# If visit api with browser, server should open cors config
# from flask_cors import CORS
# CORS(app)
 
# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)

User = setUpDB(app)

def printRequestUser(memFunc):
    def wrapper():
        r = memFunc()
        jwt_certificated_data = get_jwt_identity()
        jwt_certificated_data = json.loads(jwt_certificated_data)
        print(f"Welcome back {jwt_certificated_data['username']}")
        return r
    return wrapper

@app.route('/member', methods=['GET'])
@jwt_required()
@printRequestUser
def member():    
    tokenFromHeaders = request.headers['Authorization'].split(' ')[1]
    jwt_certificated_data = get_jwt_identity()
    jwt_certificated_data = json.loads(jwt_certificated_data)
    
    return f'Welcome back {jwt_certificated_data["username"]}\n', 200

@app.route('/register', methods=['GET'])
def registerGet():
    return 'This endpoint to show registerPage.html\n', 200
    

@app.route('/register', methods=['Post'])
def registerPost():
    user = User(   
        username = request.form['username'],
        password = request.form['password'],
        realname = request.form['realname'],
        email = request.form['email'],
    )
    searchEmail = User.query.filter_by(email=request.form['email']).first()
    searchUsername = User.query.filter_by(username=request.form['username']).first()
    if not searchEmail and not searchUsername:
        addUser(app, user)
        return 'Succeed to build user\n', 201
    elif searchEmail:
        return 'Email already exists\n', 200
    elif searchUsername:
        return 'This username has been used\n', 200

@app.route('/login', methods=['GET'])
def loginGet():
    return 'This endpoint and method is to show loginPage.html\n'
        
    
@app.route('/login', methods=['POST'])   
def loginPost():
    searchData = User.query.filter_by(email=request.form['email']).first()
    if(searchData):
        if (searchData.password == request.form['password']):
            currentUser = {
                'username':searchData.username,
                'password':searchData.password,
                'realname':searchData.realname,
                'email':searchData.email
            }
            access_token = create_access_token(identity=json.dumps(currentUser), expires_delta=datetime.timedelta(minutes=15))
            return jsonify(access_token=access_token), 201
        else:
            return 'Incorrect password\n', 200
    else:
        return 'No such user was found\n', 200

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5555)

