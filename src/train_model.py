import sqlite3
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

from config import DATABASE_PATH, MODEL_PATH


def load_data():
    conn = sqlite3.connect(DATABASE_PATH)

    query = """
    SELECT
        Gender,
        "Senior Citizen",
        Partner,
        Dependents,
        "Tenure Months",
        "Phone Service",
        "Multiple Lines",
        "Internet Service",
        "Online Security",
        "Online Backup",
        "Device Protection",
        "Tech Support",
        "Streaming TV",
        "Streaming Movies",
        Contract,
        "Paperless Billing",
        "Payment Method",
        "Monthly Charges",
        "Total Charges",
        "Churn Value"
    FROM customers;
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def main():
    df = load_data()

    X = df.drop(columns = ["Churn Value"])
    y = df["Churn Value"]

    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")

    X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42,
    stratify = y,
    )

    print(f"Training samples: {X_train.shape[0]}")
    print(f"Test samples: {X_test.shape[0]}")

    categorical_features = X.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()

    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    print("\nCategorical features:")
    print(categorical_features)

    print("\nNumeric features:")
    print(numeric_features)

    # Define preprocessing pipelines for numeric and categorical features
    numeric_transformer = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

    categorical_transformer = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers = [
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )


    model = Pipeline(
        steps = [
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42))
        ]
    )

    # Train the model

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print(f"Accuracy: {accuracy:.3f}")
    print(f"ROC AUC: {roc_auc:.3f}")

    joblib.dump(model, MODEL_PATH)
    print(f"\nModel saved to:\n{MODEL_PATH}")


if __name__ == "__main__":
    main()