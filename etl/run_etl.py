import os
from dotenv import load_dotenv

from etl.extract import extract_sheet
from etl.transform import (
    clean_departments,
    clean_students,
    clean_courses,
    clean_enrollments
)
from etl.load import (
    load_departments,
    load_students,
    load_courses,
    load_enrollments
)

load_dotenv()
os.makedirs("logs", exist_ok=True)


def run():
    print("=== ETL PIPELINE START ===")

    # 1. DEPARTMENTS
    print("[1] Departments")
    df = extract_sheet("departments")
    df = clean_departments(df)
    print(f"    inserting {len(df)} departments")
    load_departments(df)

    # 2. STUDENTS
    print("[2] Students")
    df = extract_sheet("students")
    df = clean_students(df)
    print(f"    inserting {len(df)} students")
    load_students(df)

    # 3. COURSES
    print("[3] Courses")
    df = extract_sheet("courses")
    df = clean_courses(df)
    print(f"    inserting {len(df)} courses")
    load_courses(df)

    # 4. ENROLLMENTS
    print("[4] Enrollments")
    df = extract_sheet("enrollments")
    clean_df, error_df = clean_enrollments(df)
    print(f"    inserting {len(clean_df)} enrollments")
    load_enrollments(clean_df)

    if not error_df.empty:
        error_df.to_csv("logs/etl_errors.csv", index=False)
        print(f"    rejected {len(error_df)} enrollments")

    print("=== ETL PIPELINE END ===")


if __name__ == "__main__":
    run()
