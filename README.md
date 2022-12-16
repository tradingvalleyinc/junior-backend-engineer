# python-junior-backend

Hi, this is returned assignment from Sam/許君碩
Hope everything goes well!

### How to use
1. First, clone this project with branch=main 
<!-- The other branch=fullStack is to demonstrate frontend+backend with session-based authentication -->

2. At the root folder of this project, type 'docker-compose up --build' in bash CLI. Everything would be set in a few minutes.

3. There are five api in server, which are
    * [GET] '/register'     -> render registerPage.html/return a message instead
    * [POST] '/register'    -> return messages showing whether it is success to register or not
    * [GET] '/login'        -> render login.html/return a message instead
    * [POST] '/login'       -> return messages showing whether it is success to login or not
    * [GET] '/member'       -> this page is protected using Flask_jwt_extended

4. Using flask_sqlalchemy to interact with mysql on docker. All those settings are stored in 'sqlalchemy_config.py'

5. OpenAPI Spec were attached under root directory(yaml format)

6. Decorator in use to show login user name.