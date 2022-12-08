from flask import Flask, render_template, redirect, url_for, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!!</h1>'

@app.route('/member', methods=['GET'])
def member():
    user = request.args['reqArg']
    user = json.loads(user)
    # return f'Welcome, {user["username"]}'
    return render_template('memberPage.html', user = user)

@app.route('/register', methods=['GET'])
def register():
    return render_template('registerPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = {
            "username":request.form['username'],
            "password":request.form['password'],
            "realname":'Sam',
            "email":'sam@home.org'
        }
        userJSON = json.dumps(user)
        # return render_template('memberPage.html', user = user)
        return redirect(url_for('member', reqArg = userJSON))
    else: 
        return render_template('loginPage.html')

if __name__ == "__main__":
    app.run(debug = True)