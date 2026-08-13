from config import PROCESSED_DATA_PATH, DATABASE_PATH
import sqlite3
import pandas as pd

# Read cleaned dataset
df = pd.read_csv(PROCESSED_DATA_PATH)

# Create connection
conn = sqlite3.connect(DATABASE_PATH)

# Save dataframe as SQL table
df.to_sql(
    "customers", 
    conn, 
    if_exists="replace",
    index=False,
)

conn.close()

print("Database created successfully")
print(f"Database saved at:\n{DATABASE_PATH}")