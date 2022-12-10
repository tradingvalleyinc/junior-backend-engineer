from flask import Flask, render_template, redirect, url_for, request
from package.sqlalchemy_config import setUpDB, addUser
import json
app = Flask(__name__)

UserTable = setUpDB(app)


@app.route('/')
def index():
    return '<h1>Hello world!!</h1>'

@app.route('/member', methods=['GET'])
def member():
    user = request.args['reqArg']
    user = json.loads(user)
    return render_template('memberPage.html', user = user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method == 'POST'):
        
        user = UserTable(   
            username = request.form['username'],
            password = request.form['password'],
            realname = request.form['realname'],
            email = request.form['email'],
        )
        addUser(app, user)
        return redirect('/login')
    else:
        return render_template('registerPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        currentUser = None
        searchData = UserTable.query.filter_by(email=request.form['email']).first()
        if(searchData):
            currentUser = {
                "username":searchData.username,
                "password":searchData.password,
                "realname":searchData.realname,
                "email":searchData.email
            }
            if (currentUser['password'] == request.form['password']):
                resMes = 'Success to log in'
                currentUser = json.dumps(currentUser)
                return redirect(url_for('member', reqArg = currentUser))
            else:
                resMes = 'Incorrect password'
                return render_template('loginPage.html', resMes = resMes)
        else:
            resMes = 'No such user was found'
            return render_template('loginPage.html', resMes = resMes)
    else: 
        return render_template('loginPage.html')

if __name__ == "__main__":
    app.run(debug = True)