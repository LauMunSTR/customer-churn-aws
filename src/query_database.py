from config import DATABASE_PATH
import sqlite3
import pandas as pd



# Connect to database
conn = sqlite3.connect(DATABASE_PATH)

query = """
SELECT 
    Contract,
    COUNT(*) AS customers,
    ROUND(AVG("Monthly Charges"), 2) AS avg_monthly_charge,
    ROUND(AVG("Tenure Months"), 2) AS avg_tenure
FROM customers
GROUP BY Contract;
"""

df = pd.read_sql_query(query, conn)

conn.close()

print(df)