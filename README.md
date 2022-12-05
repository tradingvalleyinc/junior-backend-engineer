# flask-mysql-docker
Here are two applications for backend server setup with flask and databases: mysql on docker service.

## 1. Flask+MySQL
This is an example of docker containers for flask and mysql connection. <br>
Please follow to the link and get more explanations:<br>
https://medium.com/@waynewu_25577/docker-flask-mysql-%E5%9F%BA%E6%9C%AC%E4%B8%B2%E6%8E%A5%E6%95%99%E5%AD%B8-77eff0871954

1. To use:
First open your terminal and locate in flask-mysql folder, then type in:
```
docker pull mysql:5.7
```
```
docker run -d --name mysql-server --network my-network -e MYSQL_ROOT_PASSWORD=secret mysql:5.7
```
```
docker run -it --rm --network my-network mysql:5.7
```
It will start to build up mysql service. <br>

2. Then, open your browser and type in: 
```
http://0.0.0.0:5000/
```
You will first see an empty list for your current data, don't worry!!
You can start to interact with the database by adding, updating and deleting the data.
```
POST: (register)
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"f", "password":"f", "name":"name", "email":"f@gmail.com"}' http://0.0.0.0:5000/user

POST: (Login)
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"f", "password":"f"}' http://0.0.0.0:5000/user/login

GET: (Get Users Information) 
curl -i -H "Content-Type: application/json" -H"Authorization:Bearer TOKEN" -X GET http://0.0.0.0:5000/user


```
Then you can see some data on your browser. And also you can log in your database by typing in:
```
docker run -it --rm --network my-network mysql:5.7 sh -c 'exec mysql -h"mysql-server" -P"3306" -uroot -p"root"'
```
We store our data in "mysql" database in docker container. 
<br><br>

