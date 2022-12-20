import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def mysqlConnection():
    connection = mysql.connector.connect(
        user=os.environ.get('mysql_local_user'),
        host=os.environ.get('mysql_local_host'),
        port='3306',
        password=os.environ.get('mysql_local_password'),
        database=os.environ.get('mysql_local_database')
    )
    return connection

# cursor = connection.cursor()
# sql = 'SELECT * FROM user;'
# cursor.execute(sql)
# data = cursor.fetchall()
# print(data)
# connection.close()