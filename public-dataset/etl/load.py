import psycopg2
import os
import dotenv
import pandas as pd

dotenv.load_dotenv()

DB_URL = os.getenv("PUBLIC_DATASET_DB_URL")

def get_conn():
    return psycopg2.connect(DB_URL)


# ---------- UNIVERSITIES ----------
def load_universities(df):
    print(f"Loading {len(df)} universities...")
    conn = get_conn()
    cur = conn.cursor()

    for idx, (_, r) in enumerate(df.iterrows(), start=1):
        if idx == 1:
            print("First university row inserted")

        if idx % 100 == 0:
            print(f"Universities processed: {idx}")

        cur.execute(
            """
            INSERT INTO universities (name, country)
            VALUES (%s, %s)
            ON CONFLICT (name) DO NOTHING
            """,
            (r.university_name, r.country)
        )

    conn.commit()
    print("Universities load complete")
    cur.close()
    conn.close()



# ---------- RESTAURANTS + INSPECTIONS ----------
def load_restaurants_and_inspections(df):
    print(f"Loading {len(df)} restaurant inspections...")
    conn = get_conn()
    cur = conn.cursor()

    for idx, (_, r) in enumerate(df.iterrows(), start=1):
        if idx == 1:
            print("First restaurant row inserted")

        if idx % 100 == 0:
            print(f"Restaurant rows processed: {idx}")

        cur.execute(
            """
            INSERT INTO restaurants (name, borough)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
            RETURNING restaurant_id
            """,
            (r.dba, r.boro)
        )

        result = cur.fetchone()
        if result:
            restaurant_id = result[0]
        else:
            cur.execute(
                "SELECT restaurant_id FROM restaurants WHERE name = %s",
                (r.dba,)
            )
            restaurant_id = cur.fetchone()[0]

        score = int(r.score) if pd.notna(r.score) else None

        cur.execute(
            """
            INSERT INTO inspections (restaurant_id, inspection_date, score, grade)
            VALUES (%s, %s, %s, %s)
            """,
            (
                restaurant_id,
                r["inspection date"],
                score,
                r.grade
            )
        )

    conn.commit()
    print("Restaurant ETL complete")
    cur.close()
    conn.close()
