import os 
import psycopg 
import csv
from datetime import date
from decimal import Decimal

insert_query="""
  insert into orders(order_id,
    order_date,
    customer_id,
  product_id,
  product_name,
 category,
  quantity,
  unit_price, 
  total_amount)
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
def transform_row(row):
    return (
        row["order_id"],
        date.fromisoformat(row["order_date"]),
        row["customer_id"],
        row["product_id"],
        row["product_name"],
        row["category"],
        int (row["quantity"]),
        Decimal(row["unit_price"]),
        Decimal(row["total_amount"])
    )
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
database_url=os.environ.get("DB_URL")
if not database_url:
    raise ValueError("DB URL is missing")

with psycopg.connect(database_url) as conn:
    print("Connected Succesfully!")
    with conn.cursor() as cur:
        with open("/home/yazid/sales/data/sales.csv","r",encoding="utf-8",newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                clean_row=transform_row(row)
                cur.execute(insert_query,clean_row)
print("Data Loaded Succesfully!")
