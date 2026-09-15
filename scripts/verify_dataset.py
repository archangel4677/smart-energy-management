import pandas as pd
import os

RAW_PATH = "/content/drive/MyDrive/SmartEnergySystems/data/raw/refit"
CLEAN_PATH = "/content/drive/MyDrive/SmartEnergySystems/data/clean"
REPORT_PATH = "/content/drive/MyDrive/SmartEnergySystems/data/report/cleaning_report.txt"

def verify_comparison(house_num):
    raw_file = f"{RAW_PATH}/House_{house_num}.csv"
    clean_file = f"{CLEAN_PATH}/House_{house_num}_clean.csv"
    if not os.path.exists(raw_file) or not os.path.exists(clean_file):
        with open(REPORT_PATH, "a") as report:
            report.write(f"⚠️ House{house_num} skipped (missing raw or cleaned file)\n\n")
        print(f"⚠️ House{house_num} skipped")
        return
    raw_df = pd.read_csv(raw_file, parse_dates=['Time'], index_col='Time')
    clean_df = pd.read_csv(clean_file, parse_dates=['Time'], index_col='Time')

    raw_rows, raw_nans = len(raw_df), raw_df.isna().sum().sum()
    clean_rows, clean_nans = len(clean_df), clean_df.isna().sum().sum()

    with open(REPORT_PATH, "a") as report:
        report.write(f"House{house_num}\n")
        report.write(f"   Raw Rows: {raw_rows}, NaNs: {raw_nans}\n")
        report.write(f"   Clean Rows: {clean_rows}, NaNs: {clean_nans}\n\n")

    print(f"✅ Verified House{house_num} → Raw {raw_rows} rows vs Clean {clean_rows} rows")

for house_num in range(1, 22):
    verify_comparison(house_num)
