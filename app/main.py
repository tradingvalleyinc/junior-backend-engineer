from module.app import app
from module.db import conn
from module.auth import bcrypt, jwt
from module.swagger import swagger
from flask import jsonify, request
from flasgger import swag_from
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import validators

## [API] SignUp
@app.route("/signUp", methods=["POST"])
@swag_from("apidocs/signUp.yml")
def signUp():
    try:
        email = request.json["email"]
        name = request.json["name"]
        username = request.json["username"]
        password = str(request.json["password"])
        login_count = 0

        # Input data validation
        if(not validators.email(email)):
            return jsonify({"data":{} ,"msg": "Error: the email is invalid."}), 400
        if(not validators.length(password, min=8, max=20)):
            return jsonify({"data":{} ,"msg": "Error: the length of password is over than 20 or less than 8."}), 400
        if(not validators.length(name, min=1, max= 20)):
            return jsonify({"data":{} ,"msg": "Error: the length of name is over than 20 or less than 1."}), 400
        if(not validators.length(username, min=1, max= 20)):
            return jsonify({"data":{} ,"msg": "Error: the length of username is over than 20 or less than 1."}), 400

        pw_hash = bcrypt.generate_password_hash(password)

        # check email exist
        uid = conn.execute("SELECT uid FROM user WHERE email = %s", email).fetchone()

        if(uid is None):
            # Insert the user data into database
            query = "INSERT INTO user (email, name, username, password, login_count) VALUES (%s, %s, %s, %s, %s)"
            data = (email, name, username, pw_hash, login_count)
            conn.execute(query, data)
            return jsonify({"data":{} ,"msg": "Sign up successfully!"}), 200
        else:
            return jsonify({"data":{} ,"msg": "The email is already exist!"}), 400
    except:
        return jsonify({"data":{} ,"msg": "The system gets error. Please contact with system administrator."}), 500


## [API] SignIn
@app.route("/signIn", methods=["POST"])
@swag_from("apidocs/signIn.yml")
def signIn():
    try:
        email = request.json["email"]
        password = str(request.json["password"])

        # Input data validation
        if(not validators.email(email)):
            return jsonify({"data":{} ,"msg": "Error: the email is invalid."}), 400
        if(not validators.length(password, min=8, max=20)):
            return jsonify({"data":{} ,"msg": "Error: the length of password is over 20 or less 8."}), 400

        # check email exist
        user = conn.execute("SELECT * FROM user WHERE email = %s", email).fetchone()

        if(user is not None):
            if(bcrypt.check_password_hash(user.password, password)):
                payload = {"uid":user.uid, "email":user.email, "username":user.username, "name":user.name}
                access_token = create_access_token(identity=payload)

                ## problem2: first_login print Welcome back
                def first_login(cb):
                    def checkFirstLogin():
                        if(user.login_count == 0):
                            cb(user.name)
                        conn.execute("UPDATE user SET login_count = login_count+1 WHERE email = %s", user.email)
                    return checkFirstLogin
                
                @first_login
                def show(name):
                    print("Welcome back " + name)
                
                show()

                return jsonify({"data":{"access_token": access_token} ,"msg": "Sign in successfully!"}), 200
            else:
                return jsonify({"data":{} ,"msg": "The password is wrong!"}), 401
        else:
            return jsonify({"data":{} ,"msg": "The email is not exist in the system."}), 401
    except:
        return jsonify({"data":{} ,"msg": "The system gets error. Please contact with system administrator."}), 500


## [API] GetUserInfo
@app.route("/userInfo", methods=["GET"])
@jwt_required()
@swag_from("apidocs/userInfo.yml")
def getUserInfo():
    try:
        current_user = get_jwt_identity()
        return jsonify({"data": current_user, "msg": "Get user information successfully."}), 200
    except:
        return jsonify({"data":{} ,"msg": "The system gets error. Please contact with system administrator."}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
