from flask import Flask, render_template, redirect, url_for, request
import json
app = Flask(__name__)

users = []

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
        user = {
            "username":request.form['username'],
            "password":request.form['password'],
            "realname":request.form['realname'],
            "email":request.form['email']
        }
        users.append(user)
        print(users)
        return redirect('/login')
    else:
        return render_template('registerPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logInUser = None
        resMes = None
        for i in range( len(users)):
            if(users[i]['email'] == request.form['email']):
                if(users[i]['password'] == request.form['password']):
                    resMes = 'Success to log in'
                    logInUser = users[i]
                    logInUser = json.dumps(logInUser)
                else:
                    resMes = 'Incorrect password'
                break
        if(logInUser):
            return redirect(url_for('member', reqArg = logInUser))
        elif(resMes):
            # print('There is no such user in db')
            return render_template('loginPage.html', resMes = resMes)
        else:
            resMes = 'No such user was found'
            return render_template('loginPage.html', resMes = resMes)
    else: 
        return render_template('loginPage.html')

if __name__ == "__main__":
    app.run(debug = True)