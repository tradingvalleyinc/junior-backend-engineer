import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# DB_URL = '  postgresql+psycopg2://  {user}: {pw}                                @{url}                                                      /{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
            # postgres://             root:   zgU2wzUeX5js7Ozd3gFlplxaolFEFQ6A    @dpg-cdt64nha6gdu249fjqe0-a.oregon-postgres.render.com      /myanalysisdb
def dbConnection():
    conn = psycopg2.connect(
        host=os.environ.get('postgre_host'),
        database=os.environ.get('postgre_database'),
        user=os.environ.get('postgre_user'),
        password=os.environ.get('postgre_password')
    )
    return conn
# dbConnection()
