# docker-compose up --build

# Test /login api with GET
    curl -X 'GET' \
    'http://127.0.0.1:5555/login' \
    -H 'accept: application/json' \

# Test /login api with Post
curl -X 'POST' \
    'http://127.0.0.1:5555/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'email=test_email&password=test_password'

# Test /register api with GET
    curl -X 'GET' \
    'http://127.0.0.1:5555/register' \
    -H 'accept: application/json'

# Test /register api with POST
    curl -X 'POST' \
    'http://127.0.0.1:5555/register' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'username=test_user2&password=test_password2&realname=test_realname2&email=test_email2'

# Test /member api with GET
    curl -X 'GET' \
    'http://127.0.0.1:5000/member' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer {valid_token_from_login_post}' \