import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print(f"AMFI codes in fund_master : {len(master_codes)}")
print(f"AMFI codes in nav_history : {len(nav_codes)}")
print(f"Missing AMFI codes : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\n✅ Every AMFI code in fund_master exists in nav_history.")
else:
    print("\nMissing Codes:")
    print(sorted(missing_codes))