from flasgger import Swagger
from module.app import app

SWAGGER_TEMPLATE = {
    "info": {
        "title": "python-junior-backend-API-Test",
        "description": "Test for API /signIn, /signUp, /UserInfo",
        "version": "1.0",
    }, 
    "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
    }
}

swagger = Swagger(app, template=SWAGGER_TEMPLATE)