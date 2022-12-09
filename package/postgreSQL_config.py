import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
def dbConnection():
    conn = psycopg2.connect(
        host=os.environ.get('postgre_host'),
        database=os.environ.get('postgre_database'),
        user=os.environ.get('postgre_user'),
        password=os.environ.get('postgre_password')
    )
    return conn
dbConnection()
