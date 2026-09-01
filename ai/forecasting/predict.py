"""
FreshStock AI - Demand Prediction

Loads the trained XGBoost model and predicts
future grocery demand.
"""

import os
import joblib
import pandas as pd


MODEL_PATH = "models/demand_model.pkl"
DATA_PATH = "data/train.csv"


def load_model():
    """Load the trained forecasting model."""

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}"
        )

    saved_data = joblib.load(MODEL_PATH)

    return saved_data["model"], saved_data["features"]


def predict_recent_demand(
    product="BEVERAGES",
    store=1
):
    """
    Predict demand using the latest available
    historical information.
    """

    model, features = load_model()

    # Load data
    df = pd.read_csv(DATA_PATH)

    df["date"] = pd.to_datetime(df["date"])

    # Select product and store
    df = df[
        (df["family"] == product) &
        (df["store_nbr"] == store)
    ].copy()

    if df.empty:
        raise ValueError(
            f"No data found for {product} at store {store}"
        )

    # Sort by date
    df = df.sort_values("date")

    # Calendar features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_weekend"] = (
        df["day_of_week"] >= 5
    ).astype(int)

    # Lag features
    df["lag_1"] = df["sales"].shift(1)
    df["lag_7"] = df["sales"].shift(7)
    df["lag_14"] = df["sales"].shift(14)

    # Rolling features
    df["rolling_7"] = (
        df["sales"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    df["rolling_14"] = (
        df["sales"]
        .shift(1)
        .rolling(14)
        .mean()
    )

    # Remove unavailable rows
    df = df.dropna()

    if df.empty:
        raise ValueError(
            "Not enough historical data for prediction."
        )

    # Take the latest record
    latest = df.iloc[-1]

    # Create input
    X = pd.DataFrame([{
        "store_nbr": latest["store_nbr"],
        "onpromotion": latest["onpromotion"],
        "year": latest["year"],
        "month": latest["month"],
        "day": latest["day"],
        "day_of_week": latest["day_of_week"],
        "is_weekend": latest["is_weekend"],
        "lag_1": latest["lag_1"],
        "lag_7": latest["lag_7"],
        "lag_14": latest["lag_14"],
        "rolling_7": latest["rolling_7"],
        "rolling_14": latest["rolling_14"]
    }])

    # Prediction
    prediction = model.predict(X)[0]

    # Demand cannot be negative
    prediction = max(0, float(prediction))

    return {
        "product": product,
        "store": int(store),
        "last_date": str(latest["date"].date()),
        "predicted_demand": round(prediction, 2)
    }


if __name__ == "__main__":

    result = predict_recent_demand(
        product="BEVERAGES",
        store=1
    )

    print("\n===================================")
    print("FreshStock AI Demand Prediction")
    print("===================================")

    print(f"Product: {result['product']}")
    print(f"Store: {result['store']}")
    print(f"Last Date: {result['last_date']}")
    print(
        f"Predicted Demand: "
        f"{result['predicted_demand']:.2f}"
    )