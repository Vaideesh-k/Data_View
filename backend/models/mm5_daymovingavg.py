import psycopg2
import pandas as pd

def get_ma5_data():
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

    # Step 2: Process data
    df['date'] = pd.to_datetime(df['date'])
    df['MA5'] = df['close'].rolling(window=5).mean()

    # Step 3: Drop rows with NaN (first 4 rows will be NaN for MA5)
    df = df.dropna(subset=["MA5"])

    # Step 4: Convert to JSON-friendly format
    result = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "ma5": round(row["MA5"], 2)
        }
        for _, row in df.iterrows()
    ]

    return result