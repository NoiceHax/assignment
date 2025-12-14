import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("SELECT current_database(), current_user;")
print("Connected to PostgreSQL")
print(cur.fetchone())

cur.close()
conn.close()
