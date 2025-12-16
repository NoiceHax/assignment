import pandas as pd

# ---------- CLEAN DATASET ----------
def clean_universities(df):
    # normalize headers
    df.columns = df.columns.str.lower().str.strip()

    # select only what exists
    df = df[[
        "university_name",
        "country",
        "year",
        "world_rank",
        "total_score"
    ]]

    # rename to match DB logic
    df = df.rename(columns={
        "world_rank": "rank",
        "total_score": "score"
    })

    # basic cleaning
    df["university_name"] = df["university_name"].str.strip()
    df["country"] = df["country"].str.strip()

    return df.dropna(subset=["university_name", "country"])


# ---------- MESSY DATASET ----------
def clean_restaurants(df):
    df.columns = df.columns.str.lower().str.strip()

    # keep only relevant columns
    df = df[[
        "camis",
        "dba",
        "boro",
        "inspection date",
        "score",
        "grade"
    ]]

    # clean text
    df["dba"] = df["dba"].str.upper().str.strip()
    df["boro"] = df["boro"].str.strip()

    # fix dates
    df["inspection date"] = pd.to_datetime(
        df["inspection date"], errors="coerce"
    )

    # invalid scores -> NULL
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df.loc[(df["score"] < 0) | (df["score"] > 100), "score"] = None


    return df.dropna(subset=["dba"])
