import pandas as pd


# Path to the raw dataset

DATA_PATH = "data/raw/Telco_customer_churn.xlsx"

# Load the dataset
df = pd.read_excel(DATA_PATH)

# Basic information
print("Dataset shape:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nColumn names:")
print(df.columns)

print("\nUnique values per column:")
print(df.nunique())

print("\nSummary statistics:")
print(df.describe())