import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading dataset...\n")

# ============================
# Load CSV
# ============================

df = pd.read_csv("sales_data.csv")

# ============================
# Data Cleaning
# ============================

df.columns = df.columns.str.strip().str.lower()

df = df.drop_duplicates()

df = df.dropna()

print("Data Cleaned Successfully!")

# ============================
# KPIs
# ============================

print("\n========== KPIs ==========")

total_sales = df["sales"].sum()
average_sales = df["sales"].mean()
highest_sales = df["sales"].max()
lowest_sales = df["sales"].min()

total_regions = df["region"].nunique()
total_counties = df["county"].nunique()
total_salespersons = df["salesperson"].nunique()

print(f"Total Sales           : {total_sales}")
print(f"Average Sales         : {average_sales:.2f}")
print(f"Highest Sales         : {highest_sales}")
print(f"Lowest Sales          : {lowest_sales}")
print(f"Total Regions         : {total_regions}")
print(f"Total Counties        : {total_counties}")
print(f"Total Salespersons    : {total_salespersons}")

# ============================
# Region-wise Sales
# ============================

region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ============================
# County-wise Sales
# ============================

county_sales = df.groupby("county")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
county_sales.plot(kind="bar")
plt.title("Sales by County")
plt.xlabel("County")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ============================
# Salesperson-wise Sales
# ============================

salesperson_sales = df.groupby("salesperson")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(12,5))
salesperson_sales.plot(kind="bar")
plt.title("Sales by Salesperson")
plt.xlabel("Salesperson")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ============================
# Top 5 Salespersons
# ============================

print("\n========== Top 5 Salespersons ==========\n")

print(
    salesperson_sales
    .sort_values(ascending=False)
    .head(5)
)

print("\nAnalysis Completed Successfully!")