import os
import pandas as pd

print("Program started...")

# Path to raw data folder
data_folder = "data/raw"

# List all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    print("=" * 60)
    print(f"Dataset: {file}")
    print("=" * 60)

    file_path = os.path.join(data_folder, file)

    try:
        df = pd.read_csv(file_path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")

    except Exception as e:
        print(f"Error reading {file}: {e}")