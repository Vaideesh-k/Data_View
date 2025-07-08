import psycopg2
import pandas as pd

def get_lower_shadow_data():
    # Step 1: Connect and fetch OHLC from PostgreSQL
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, open, close, low FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Step 2: Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Calculate Lower Shadow Size
    df['Lower_Shadow_Size'] = df[['open', 'close']].min(axis=1) - df['low']

    # Step 4: Format as JSON-friendly list
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "lower_shadow_size": round(row["Lower_Shadow_Size"], 2)
        }
        for _, row in df.iterrows()
    ]

    return result