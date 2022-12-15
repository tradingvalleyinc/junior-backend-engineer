# If developer edit the source code, docker images have to be deleted and rebuild
# (Uncomment two commands below)
# docker rmi python-junior-backend-flask-server
# docker rmi python-junior-backend-mysql-server

docker-compose up


# Command to check whether data are stored in mysql-server
# docker exec -it mysql_container sh -c 'mysql -u localUser -p"password"'
# use tradingValley_userdb;
# SELECT * FROM user;

# To delect all container and images
# docker rm $(docker ps -a -q)
# docker rmi $(docker images -q)
