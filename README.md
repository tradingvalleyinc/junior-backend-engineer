# python-junior-backend

## Set up

1.  `cd app/`
2.  `mv .env_example .env`
3.  Confirm the port 5001 and port 32000 are not used in your device.
4.  `docker-compose up -d`

<br>
* Your device needs to install docker, docker-compose first.
<br>

---

## Test the API (/signIn, /signuUp, /userInfo)

### \*Method 1: Swagger API

[http://<your_server>:5001/apidocs/](http://yourserver:5001/apidocs/)
<br>

### Method 2: curl

/signUp

```bash
curl --location --request POST 'http://<your_server>:5001/signUp' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "1@gmail.com",
    "name": "abc",
    "username": "abc",
    "password": "12345678"
}'
```

/signIn

```bash
curl --location --request POST 'http://<your_server>:5001/signIn' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "1@gmail.com",
    "password": "12345678"
}'
```
/userInfo

```bash
curl --location --request GET 'http://<your_server>/userInfo' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MDg3MjkwMSwianRpIjoiNzkzNTUwNWYtODlmZC00ZDBlLWFhYTEtYzAxNTMwMDRmMjM1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1aWQiOjEsImVtYWlsIjoiMUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImFiYyIsIm5hbWUiOiJhYmMifSwibmJmIjoxNjcwODcyOTAxLCJleHAiOjE2NzA4NzM4MDF9.fKBYUcc66wOHVci3XqmRZvTB6i6qT3YzKb3jVvwJMVg'
```
*Note: Change <your_server> to your server domain name or IP & --data-raw's json data.

<br>

### Method 3: postman

/signUp

```
Method: POST
URL: "http://<your_server>:5001/signUp"
requestBody:
{
    "email": "1@gmail.com",
    "name": "abc",
    "username": "abc",
    "password": "12345678"
}
```

/signIn

```
Method: POST
URL: "http://<your_server>:5001/signIn"
requestBody:
{
    "email": "1@gmail.com",
    "password": "12345678"
}
```

/userInfo

```
Method: GET
URL: "http://<your_server>:5001/userInfo"
Authorization:
    Type: Bearer Token
    Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MDg3MjkwMSwianRpIjoiNzkzNTUwNWYtODlmZC00ZDBlLWFhYTEtYzAxNTMwMDRmMjM1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1aWQiOjEsImVtYWlsIjoiMUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImFiYyIsIm5hbWUiOiJhYmMifSwibmJmIjoxNjcwODcyOTAxLCJleHAiOjE2NzA4NzM4MDF9.fKBYUcc66wOHVci3XqmRZvTB6i6qT3YzKb3jVvwJMVg
```

<br>
*Note: Change <your_server> to your server domain name or IP & --data-raw's json data.

---

## Requirement checklist

- [x] 1. Implement a membership website
  - [x] Flask framework
  - [x] POST /signUp
  - [x] POST /signIn
  - [x] GET /userInfo (Authentication by Bearer Token)
  - [x] Database Table field contains (username, password ,name, email)
  - [x] ORM SQLAlchemy
  - [x] Input data validation
  - [x] OpenAPI spec: swagger
- [x] 2. Implement the decorator in /signIn API
  - [x] First login print "Welcome back {name}".
- [x] Deploy by docker
