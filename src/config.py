from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Telco_customer_churn.xlsx"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "customer_churn_clean.csv"
DATABASE_PATH = PROJECT_ROOT / "data" / "customer_churn.db"

# Models
MODEL_PATH = PROJECT_ROOT / "models" / "customer_churn_model.pkl"