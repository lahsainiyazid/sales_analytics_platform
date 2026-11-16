import os 
import psycopg 
import csv
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
database_url=os.environ.get("DB_URL")
if not database_url:
    raise ValueError("DB URL is missing")

with psycopg.connect(database_url) as conn:
    print("Connected successfully!")
    with open("/home/yazid/sales/data/sales.csv","r",encoding="utf-8",newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(row)
