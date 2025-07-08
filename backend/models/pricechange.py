import psycopg2
import numpy as np
import pandas as pd

def get_price_change_data():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    # Fetch open and close prices
    df = pd.read_sql("SELECT date, open, close FROM spy ORDER BY date ASC;", conn)
    conn.close()

    # Calculate price change percentage
    df['Price_Change'] = (df['close'] - df['open']) / df['open']

    # Prepare JSON output
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "price_change": round(row["Price_Change"], 6)  # 6 decimal places
        }
        for _, row in df.iterrows()
    ]

    return result