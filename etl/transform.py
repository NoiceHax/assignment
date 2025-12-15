import pandas as pd


def to_int(series):
    return pd.to_numeric(series, errors="coerce").astype("Int64")


def clean_departments(df):
    df["department_id"] = to_int(df["department_id"])
    df["name"] = df["name"].astype(str)
    return df.dropna(subset=["department_id", "name"])


def clean_students(df):
    df["student_id"] = to_int(df["student_id"])
    df["department_id"] = to_int(df["department_id"])
    df["email"] = df["email"].astype(str)
    df["name"] = df["name"].astype(str)
    return df.dropna(subset=["student_id", "email"])


def clean_courses(df):
    df["course_id"] = to_int(df["course_id"])
    df["department_id"] = to_int(df["department_id"])
    df["name"] = df["name"].astype(str)
    return df.dropna(subset=["course_id", "department_id"])


def clean_enrollments(df):
    errors = []

    for col in ["enrollment_id", "student_id", "course_id"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["grade"] = pd.to_numeric(df["grade"], errors="coerce")

    bad_grade = ~df["grade"].between(0, 100)
    errors.extend(df[bad_grade].assign(error="Invalid grade").to_dict("records"))
    df = df[~bad_grade]

    missing_fk = df[["student_id", "course_id"]].isna().any(axis=1)
    errors.extend(df[missing_fk].assign(error="Missing FK").to_dict("records"))
    df = df[~missing_fk]

    df = df.astype({
        "enrollment_id": int,
        "student_id": int,
        "course_id": int,
        "grade": float
    })

    return df, pd.DataFrame(errors)
