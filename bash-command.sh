docker pull python

docker pull mysql

docker-compose up


docker exec -it server_container sh -c 'curl http://127.0.0.1:5555/register; \
curl http://127.0.0.1:5555/login; \
curl -X POST http://127.0.0.1:5555/register -d "username=curl_user&password=curl_password&realname=curl_realname&email=curl@email.com"; \
curl -X POST http://127.0.0.1:5555/login -d "email=curl@email.com&password=curl_password";'

# docker exec -it mysql_container sh -c 'mysql -u localUser -p"password"'


# use tradingValley_userdb

# SELECT * FROM user;




# Common commands: 
# POST
# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Test", "notify":"xxxxxx@gmail.com"}' http://0.0.0.0:5000/
# PUT
# curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Update", "is_completed":1, "notify":"xxxxxx@gmail.com", name:<Your Name>}' http://0.0.0.0:5000/<id>
# GET ALL
# curl -v http://0.0.0.0:5000/
# GET
# curl -v http://0.0.0.0:5000/<id>
# DELETE ALL
# curl -v -X DELETE http:/0.0.0.0:5000/
# DELETE
# curl -v -X DELETE http:/0.0.0.0:5000/<id>

# Enter Mysql
# docker run -it --rm --network my-network mysql:5.7 sh -c 'exec mysql -h"mysql-server" -P"3306" -uroot -p"secret"'



# Construct a network
# docker network create -d bridge my-network

# MYSQL server
# Pull mysql image from Docker Hub
# docker pull mysql:5.7
# Run the mysql container
# docker run -d --name mysql-server --network my-network -e MYSQL_ROOT_PASSWORD=secret mysql:5.7


# Flask server
# Build flask image
# docker build -t flask-app .
# Run the flask server
# docker run -p 5050:5050 --network my-network -v "$PWD":/app -d flask-app
