from extract import extract_csv
from transform import clean_universities, clean_restaurants
from load import load_universities, load_restaurants_and_inspections

print("=== ETL START ===")

uni_df = extract_csv("data/universities.csv")
uni_df = clean_universities(uni_df.head(2000))
load_universities(uni_df)

rest_df = extract_csv("data/restaurant_inspections.csv")
rest_df = clean_restaurants(rest_df.head(2000))
load_restaurants_and_inspections(rest_df)

print("=== ETL COMPLETE ===")
