from module.app import app
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager

# for password bcrypt
bcrypt = Bcrypt(app)

# for access_token
load_dotenv()
jwt = JWTManager()
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
jwt.init_app(app)


