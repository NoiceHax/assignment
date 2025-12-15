import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("SELECT current_database(), current_user,inet_server_addr();")
print("Connected to NeonDB")
print(cur.fetchone())
cur.execute("SELECT current_setting('neon.branch_id', true);")
print("BRANCH FROM PYTHON:", cur.fetchone())
cur.close()
conn.close()

# import os
# print(os.environ.get("DATABASE_URL"))
