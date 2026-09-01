"""
FreshStock AI - Demand Forecasting

Uses historical grocery sales data to train an XGBoost
demand forecasting model with lag and rolling features.
"""

import os
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_PATH = "data/train.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "demand_model.pkl")

PRODUCT = "BEVERAGES"


# ---------------------------------------------------------
# Load and prepare data
# ---------------------------------------------------------

def prepare_data(csv_path=DATA_PATH, product=PRODUCT):
    """Load dataset and create forecasting features."""

    print("Loading dataset...")

    df = pd.read_csv(csv_path)

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Select product family
    df = df[df["family"] == product].copy()

    # Sort correctly
    df = df.sort_values(["store_nbr", "date"])

    # Calendar features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    # -----------------------------------------------------
    # Lag features
    # -----------------------------------------------------

    # Previous day's sales
    df["lag_1"] = df.groupby("store_nbr")["sales"].shift(1)

    # Sales 7 days ago
    df["lag_7"] = df.groupby("store_nbr")["sales"].shift(7)

    # Sales 14 days ago
    df["lag_14"] = df.groupby("store_nbr")["sales"].shift(14)

    # -----------------------------------------------------
    # Rolling features
    # -----------------------------------------------------

    # IMPORTANT:
    # shift(1) prevents today's sales from being used
    # to predict today's sales.
    df["rolling_7"] = (
        df.groupby("store_nbr")["sales"]
        .transform(lambda x: x.shift(1).rolling(7).mean())
    )

    df["rolling_14"] = (
        df.groupby("store_nbr")["sales"]
        .transform(lambda x: x.shift(1).rolling(14).mean())
    )

    # Remove rows where lag/rolling values are unavailable
    df = df.dropna()

    return df


# ---------------------------------------------------------
# Train model
# ---------------------------------------------------------

def train_model(csv_path=DATA_PATH, product=PRODUCT):

    df = prepare_data(csv_path, product)

    print(f"Product: {product}")
    print(f"Rows after feature engineering: {len(df)}")

    # Features used by model
    features = [
        "store_nbr",
        "onpromotion",
        "year",
        "month",
        "day",
        "day_of_week",
        "is_weekend",
        "lag_1",
        "lag_7",
        "lag_14",
        "rolling_7",
        "rolling_14"
    ]

    X = df[features]
    y = df["sales"]

    # -----------------------------------------------------
    # Time-based train/test split
    # -----------------------------------------------------

    split = int(len(df) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    print(f"Training rows: {len(X_train)}")
    print(f"Testing rows: {len(X_test)}")

    # -----------------------------------------------------
    # XGBoost model
    # -----------------------------------------------------

    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=-1
    )

    print("\nTraining XGBoost model...")

    model.fit(X_train, y_train)

    # -----------------------------------------------------
    # Evaluation
    # -----------------------------------------------------

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5

    print("\n===================================")
    print("FreshStock AI Forecasting Results")
    print("===================================")
    print(f"Product: {product}")
    print(f"Training rows: {len(X_train)}")
    print(f"Testing rows: {len(X_test)}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    # -----------------------------------------------------
    # Save model
    # -----------------------------------------------------

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(
        {
            "model": model,
            "features": features,
            "product": product
        },
        MODEL_PATH
    )

    print(f"\nModel saved successfully:")
    print(MODEL_PATH)

    return model


# ---------------------------------------------------------
# Run directly
# ---------------------------------------------------------

if __name__ == "__main__":
    train_model()