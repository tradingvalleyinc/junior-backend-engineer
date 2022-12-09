from flask import Flask, render_template, redirect, url_for, request
from package.postgreSQL_config import dbConnection
import json
app = Flask(__name__)

# cur = dbConnection()
conn = dbConnection()
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
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO userinformationtable (username, password, realname, email)'
            'VALUES (%s,%s,%s,%s)', 
            (request.form['username'],
            request.form['password'],
            request.form['realname'],
            request.form['email'])
            )
        conn.commit()
        cur.close()
        return redirect('/login')
    else:
        return render_template('registerPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        currentUser = None
        resMes = None
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM userinformationtable WHERE email = %s', 
            (request.form['email'],))
        searchData = cur.fetchone()
        print(searchData)
        cur.close()
        if(searchData):
            currentUser = {
                "username":searchData[1],
                "password":searchData[2],
                "realname":searchData[3],
                "email":searchData[4]
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