import psycopg2
import pandas as pd

def get_volume_change_data():
    # Connect to PostgreSQL and fetch date & volume
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    query = "SELECT date, volume FROM spy ORDER BY date ASC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Convert date column to datetime and calculate volume % change
    df['date'] = pd.to_datetime(df['date'])
    df['Volume_Change_Percent'] = df['volume'].pct_change() * 100
    df.dropna(inplace=True)  # Drop the first row with NaN

    # Convert to list of dictionaries
    data = df[['date', 'Volume_Change_Percent']].copy()
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')

    result = data.to_dict(orient='records')
    return result