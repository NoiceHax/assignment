import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Basic connection info
cur.execute("SELECT current_database(), current_user, inet_server_addr();")
print("Connected to PostgreSQL")
print(cur.fetchone())

cur.execute("SELECT current_setting('neon.branch_id', true);")
print("BRANCH FROM PYTHON:", cur.fetchone())

cur.close()
conn.close()
