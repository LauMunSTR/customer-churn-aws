from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
import pandas as pd



# Load data
df = pd.read_excel(RAW_DATA_PATH)

# Remove columns that would leak future information
columns_to_drop = ["Churn Score",
                   "Churn Reason",
                    "CLTV",
]

df = df.drop(columns=columns_to_drop)
# Convert Total Charges to numeric
df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")


# Save cleaned dataset
df.to_csv(PROCESSED_DATA_PATH, index=False)

print("Dataset cleaned successfully")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Saved to: {PROCESSED_DATA_PATH}")
