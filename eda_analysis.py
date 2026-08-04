import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading Dataset...\n")

# -------------------------
# Load Dataset
# -------------------------
df = pd.read_csv("sales_data.csv")

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

print("Original Dataset Shape:", df.shape)

# -------------------------
# Missing Values
# -------------------------
print("\n========== Missing Values ==========")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# -------------------------
# Duplicate Removal
# -------------------------
print("\n========== Duplicate Rows ==========")
print(df.duplicated().sum())

df = df.drop_duplicates()

# -------------------------
# Data Validation
# -------------------------
print("\n========== Data Validation ==========")

print("\nNegative Sales Values:")
print(df[df["sales"] < 0])

print("\nUnique Regions:")
print(df["region"].unique())

# -------------------------
# Basic Statistics
# -------------------------
print("\n========== Basic Statistics ==========")

print(df.describe())

# -------------------------
# Outlier Detection
# -------------------------

Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["sales"] < lower) | (df["sales"] > upper)]

print("\n========== Outliers ==========")
print(outliers)

# -------------------------
# Correlation
# -------------------------

print("\n========== Correlation ==========")

numeric_df = df.select_dtypes(include=np.number)

print(numeric_df.corr())

# -------------------------
# Trend Analysis
# -------------------------

region_sales = df.groupby("region")["sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="line", marker="o")
plt.title("Sales Trend Across Regions")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------
# Save Clean Dataset
# -------------------------

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_sales_data.csv")

print("\nEDA Completed Successfully!")