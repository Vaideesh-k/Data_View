import psycopg2
import pandas as pd

def get_ema10_data():
    # Step 1: Connect to PostgreSQL and load data
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, close FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Step 2: Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Calculate 10-Day Exponential Moving Average (EMA10)
    df['EMA10'] = df['close'].ewm(span=10, adjust=False).mean()

    # Step 4: Drop NaN rows (initial rows)
    df = df.dropna(subset=["EMA10"])

    # Step 5: Convert to JSON-friendly format
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "ema10": round(row["EMA10"], 2)
        }
        for _, row in df.iterrows()
    ]

    return result