import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

creds = Credentials.from_service_account_file(
    r"C:\Users\Chandan\Desktop\service_account.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

SHEET_URL = "https://docs.google.com/spreadsheets/d/1j2IkRIOeDJ-eYXVX23CuQFI6N9E-Bey3G1sqW5RHDHc/edit?gid=0#gid=0"

sheet = client.open_by_url(SHEET_URL).sheet1

data = sheet.get_all_values()
df = pd.DataFrame(data)

print(df.head())