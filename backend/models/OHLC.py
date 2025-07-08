import psycopg2
import pandas as pd

def get_ohlc_mean_data():
    # Step 1: Connect to PostgreSQL and fetch OHLC data
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, open, high, low, close FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Step 2: Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Calculate OHLC Mean
    df['OHLC_Mean'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4

    # Step 4: Format as JSON-ready list
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "ohlc_mean": round(row["OHLC_Mean"], 2)
        }
        for _, row in df.iterrows()
    ]

    return result