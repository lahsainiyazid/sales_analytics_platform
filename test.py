import os
import psycopg
from dotenv import load_dotenv,find_dotenv 


_=load_dotenv(find_dotenv())
DB=os.environ.get("DB_URL")
def test_db():
    with psycopg.connect(DB) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1+1");
            result=cur.fetchone();
            print (result);


if __name__=="__main__":
    test_db()



