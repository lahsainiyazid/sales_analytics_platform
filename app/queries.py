from dotenv import load_dotenv,find_dotenv 
import os 
import psycopg
from psycopg.rows import dict_row
_=load_dotenv(find_dotenv())

db_url=os.environ.get("DB_URL")

def get_all():
    with psycopg.connect(db_url,row_factory=dict_row) as conn:
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
            return row[0]
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
            return row[0]
def get_num_sales():
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            Select count(*)
            from orders;
                        """)
            row=cur.fetchone()
            return row[0]


def get_avg_val():
    with psycopg.connect(db_url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
               SELECT round(AVG (total_amount),2)
               from orders;
                        """)
            rows=cur.fetchall()
            return rows;

def get_rev_by_cat():
    with psycopg.connect(db_url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT round(avg(total_amount),2)
            from orders 
            group by category ;
                        """)
            rows=cur.fetchall()
            return rows

def get_latest_sell():
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT *
            from orders 
            order by order_date desc 
            limit 1;
            """)
            row=cur.fetchone()
            return row
