import psycopg2
import pandas as pd

def get_upper_shadow_data():
    # Step 1: Connect and fetch OHLC data
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, open, close, high FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Step 2: Process Data
    df['date'] = pd.to_datetime(df['date'])
    df['Upper_Shadow_Size'] = df['high'] - df[['open', 'close']].max(axis=1)

    # Step 3: Convert to JSON-friendly list of dicts
    shadow_data = df.dropna().apply(
        lambda row: {
            "date": row["date"].strftime("%Y-%m-%d"),
            "upper_shadow": round(row["Upper_Shadow_Size"], 2)
        },
        axis=1
    ).tolist()

    return shadow_data