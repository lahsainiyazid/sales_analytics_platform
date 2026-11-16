from dotenv import load_dotenv,find_dotenv 
import os


_=load_dotenv(find_dotenv())
DB=os.environ.get("DB_URL")
print(DB)



