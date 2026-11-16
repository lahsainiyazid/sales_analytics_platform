from dotenv import load_dotenv,find_dotenv 
import os 
import psycopg
_=load_dotenv(find_dotenv())

db_url=os.environ.get("DB_URL")

def get_all():
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * from orders;")
            rows=cur.fetchall()
            return rows

def get_tot_rev():
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT sum (total_amount) as total_revenue
            from orders;
             """)
            row=cur.fetchone()
            return row
def get_num_customers():
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                Select count (distinct customer_id)
                from orders;
                """
            )
            row=cur.fetchone()
            return row
