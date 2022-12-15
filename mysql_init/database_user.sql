use tradingValley_userdb;

CREATE TABLE user(
id serial PRIMARY KEY,
username varchar(50) NOT NULL UNIQUE,
password varchar(150) NOT NULL,
realname varchar(50) NOT NULL,
email varchar(100) NOT NULL UNIQUE,
date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO user(username, password, realname, email)
VALUES ('test_user', 'test_password', 'test_realname', 'test@email.com');