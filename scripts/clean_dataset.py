import pandas as pd
import os
RAW_PATH = "/content/drive/MyDrive/SmartEnergySystems/data/raw/refit"
def clean_dataset(input_path, output_folder="/content/drive/MyDrive/SmartEnergySystems/data/clean"):
    
    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_csv(input_path, parse_dates=['Time'], index_col='Time')
    df = df.resample('h').mean()

    if 'Aggregate' in df.columns:
        df['Aggregate'] = df['Aggregate'].interpolate().ffill()

    appliance_cols = [col for col in df.columns if col != 'Aggregate']
    df[appliance_cols] = df[appliance_cols].ffill()

    filename = os.path.basename(input_path).replace(".csv", "_clean.csv")
    output_path = os.path.join(output_folder, filename)
    df.to_csv(output_path)

    print(f"✅ Cleaned file saved to: {output_path}")
for house_num in range(1, 22):  # 1 to 21 inclusive
    file_path = f"{RAW_PATH}/House_{house_num}.csv"
    if os.path.exists(file_path):
        clean_dataset(file_path)
    else:
        print(f"⚠️ File not found: {file_path}")