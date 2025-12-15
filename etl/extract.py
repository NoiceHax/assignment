import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SHEET_URL = "https://docs.google.com/spreadsheets/d/1j2IkRIOeDJ-eYXVX23CuQFI6N9E-Bey3G1sqW5RHDHc/edit"


def extract_sheet(sheet_name: str) -> pd.DataFrame:
    creds = Credentials.from_service_account_file(
        r"C:\Users\Chandan\Desktop\service_account.json",
        scopes=SCOPES
    )
    client = gspread.authorize(creds)

    sheet = client.open_by_url(SHEET_URL)
    worksheet = sheet.worksheet(sheet_name)

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    print(f"    extracted {len(df)} rows from sheet '{sheet_name}'")
    return df
