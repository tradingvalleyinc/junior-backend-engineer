from flask import Flask, render_template, redirect, request
from package.sqlalchemy_config import setUpDB, addUser
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UserTable = setUpDB(app)

@login_manager.user_loader
def load_user(user_id):
    return UserTable.query.get(user_id)


@app.route('/')
def index():
    return '<h1>Hello world!!</h1>'

@app.route('/member-<username>', methods=['GET'])
@login_required
def member(username):
    
    # To convert class(current_user) to object(user) so that html could read
    user = {
        'username':current_user.username,
        'password':current_user.password,
        'realname':current_user.realname,
        'email':current_user.email
    }
    
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
        searchData = UserTable.query.filter_by(email=request.form['email']).first()
        if(searchData):
            if (searchData.password == request.form['password']):
                resMes = 'Success to log in'
                login_user(searchData)
                generatedURL = f'member-{searchData.username}'
                return redirect(generatedURL)
            else:
                resMes = 'Incorrect password'
                return render_template('loginPage.html', resMes = resMes)
        else:
            resMes = 'No such user was found'
            return render_template('loginPage.html', resMes = resMes)
    else: 
        return render_template('loginPage.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug = True)