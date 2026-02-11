"""
Simple ETL example:
- Extract: read orders from a CSV file
- Transform: clean columns and compute daily revenue
- Load: write aggregated results to another CSV file
"""

from pathlib import Path

import pandas as pd


def extract(csv_path: Path) -> pd.DataFrame:
    """Read raw orders CSV into a DataFrame."""
    df = pd.read_csv(csv_path)
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data and compute daily revenue."""
    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Basic cleaning
    df = df.dropna(subset=["order_date", "price", "quantity"])

    # Ensure correct types
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    # Compute revenue
    df["revenue"] = df["price"] * df["quantity"]

    # Aggregate to daily revenue
    daily = (
        df.groupby(df["order_date"].dt.date)["revenue"]
        .sum()
        .reset_index(name="daily_revenue")
    )

    return daily


def load(df: pd.DataFrame, output_path: Path) -> None:
    """Write the transformed data to a CSV file."""
    df.to_csv(output_path, index=False)


def main() -> None:
    project_root = Path(__file__).parent
    raw_path = project_root / "raw_orders.csv"
    output_path = project_root / "daily_revenue.csv"

    if not raw_path.exists():
        raise FileNotFoundError(
            f"Input file {raw_path} not found. "
            "Create a raw_orders.csv file in this folder to test the ETL."
        )

    orders = extract(raw_path)
    daily_revenue = transform(orders)
    load(daily_revenue, output_path)
    print(f"Wrote {len(daily_revenue)} rows to {output_path}")


if __name__ == "__main__":
    main()
