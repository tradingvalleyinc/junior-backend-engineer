from flask import Flask, render_template, redirect, request, flash
from package.sqlalchemy_config import setUpDB, addUser
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    # create_refresh_token, jwt_refresh_token_required,
    get_jwt_identity
    )
import datetime
from flask import jsonify
import json

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)

UserTable = setUpDB(app)


@app.route('/', methods=["GET"])
def index():
    print('hello')
    return redirect('http://127.0.0.1:5000/login')

@app.route('/member', methods=['GET'])
@jwt_required()

def member():    
    tokenFromHeaders = request.headers['Authorization'].split(' ')[1]
    # print(tokenFromHeaders)
    jwt_certificated_data = get_jwt_identity()
    jwt_certificated_data = json.loads(jwt_certificated_data)
    
    return render_template('memberPage.html', user = jwt_certificated_data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method == 'POST'):
        user = UserTable(   
            username = request.form['username'],
            password = request.form['password'],
            realname = request.form['realname'],
            email = request.form['email'],
        )
        searchEmail = UserTable.query.filter_by(email=request.form['email']).first()
        searchUsername = UserTable.query.filter_by(username=request.form['username']).first()
        if not searchEmail and not searchUsername:
            addUser(app, user)
            return redirect('/login')
        elif searchEmail:
            flash('Email already exists')
            return render_template('registerPage.html')
        elif searchUsername:
            flash('This username has been used')
            return render_template('registerPage.html')
    else:
        return render_template('registerPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        searchData = UserTable.query.filter_by(email=request.form['email']).first()
        # print(searchData)
        if(searchData):
            if (searchData.password == request.form['password']):
                # flash('Success to log in')
                currentUser = {
                    'username':searchData.username,
                    'password':searchData.password,
                    'realname':searchData.realname,
                    'email':searchData.email
                }
                access_token = create_access_token(identity=json.dumps(currentUser), expires_delta=datetime.timedelta(minutes=15))
                return jsonify(access_token=access_token)
    
                # generatedURL = f'/member-{searchData.username}/'
                # return redirect(f"http://127.0.0.1:5000/member-{searchData.username}")
            else:
                flash('Incorrect password')
                return render_template('loginPage.html')
        else:
            flash('No such user was found')
            return render_template('loginPage.html')
    else: 
        return render_template('loginPage.html')

# @app.route('/logout', methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect('/login')

if __name__ == "__main__":
    app.run(debug = True, port=5000)