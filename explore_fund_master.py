import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER DATASET SUMMARY")
print("=" * 60)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:", df["fund_house"].nunique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Categories:")
print(df["risk_category"].unique())

print("\nFirst 10 AMFI Codes:")
print(df["amfi_code"].head(10))

print("\nDataset Shape:")
print(df.shape)