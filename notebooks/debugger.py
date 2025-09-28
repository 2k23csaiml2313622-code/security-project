import pandas as pd

# Path looks correct
file_path = 'artifacts/09_27_2025_07_26_17/data_ingestion/ingested/train.csv' 

try:
    # --- FINAL CHANGE IS HERE ---
    df = pd.read_csv(file_path, encoding='latin1') 
    
    print("✅ Successfully read the CSV file.")
    print(f"👉 The train.csv file has {len(df.columns)} columns.")
    print("\nHere are the column names found in the file:")
    print(list(df.columns))
except FileNotFoundError:
    print(f"❌ Error: Could not find the file at '{file_path}'. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")