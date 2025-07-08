import psycopg2
import pandas as pd

def get_candle_body_data():
    # Step 1: Fetch open & close from PostgreSQL
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, open, close FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Step 2: Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Calculate Candle Body Size
    df['Candle_Body_Size'] = (df['close'] - df['open']).abs()

    # Step 4: Convert to JSON-friendly format
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "candle_body_size": round(row["Candle_Body_Size"], 2)
        }
        for _, row in df.iterrows()
    ]

    return result