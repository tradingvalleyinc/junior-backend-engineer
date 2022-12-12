from module.app import app
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PW = os.getenv("MYSQL_PW")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

conn = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PW}@{MYSQL_HOST}/{MYSQL_DATABASE}")
