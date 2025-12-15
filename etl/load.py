import psycopg2
import os
import pandas as pd
from .extract import extract_sheet

def insert_rows(query, rows):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    count = 0

    for row in rows:
        try:
            cur.execute(query, row)
            count += 1
        except Exception as e:
            print("    insert failed:", e)
            conn.rollback()
        else:
            conn.commit()

    cur.close()
    conn.close()
    return count



def load_departments(df):
    rows = []
    for r in df.itertuples():
        rows.append((int(r.department_id), r.name))

    return insert_rows(
        "INSERT INTO departments (department_id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING",
        rows
    )



def load_students(df):
    df = extract_sheet("students")
    df = df[df["status"] == "READY"]

    rows = []

    for r in df.itertuples():
        rows.append((
            int(r.student_id),
            r.name,
            r.email
        ))

    return insert_rows(
        """
        INSERT INTO students (student_id, name, email)
        VALUES (%s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        rows
    )




def load_courses(df):
    return insert_rows(
        "INSERT INTO courses (course_id, name, department_id) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
        [(int(r.course_id), r.name, int(r.department_id)) for r in df.itertuples()]
    )


def load_enrollments(df):
    return insert_rows(
        "INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (%s, %s, %s, %s)",
        [(int(r.enrollment_id), int(r.student_id), int(r.course_id), float(r.grade)) for r in df.itertuples()]
    )
