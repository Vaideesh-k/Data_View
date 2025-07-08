import psycopg2
import pandas as pd

def get_rsi_data():
    # Step 1: Connect and fetch data
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    df = pd.read_sql("SELECT date, close FROM spy ORDER BY date ASC;", conn)
    conn.close()

    # Step 2: Prepare dataframe
    df['date'] = pd.to_datetime(df['date'])
    df['price_change'] = df['close'].diff()

    # Step 3: Calculate gains and losses
    df['gain'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
    df['loss'] = df['price_change'].apply(lambda x: -x if x < 0 else 0)

    # Step 4: Rolling averages
    window = 14
    avg_gain = df['gain'].rolling(window=window).mean()
    avg_loss = df['loss'].rolling(window=window).mean()

    # Step 5: RSI Calculation
    rs = avg_gain / avg_loss
    df['RSI_14'] = 100 - (100 / (1 + rs))

    # Step 6: Return JSON data (drop NaN rows)
    rsi_data = df.dropna().apply(
        lambda row: {
            "date": row["date"].strftime("%Y-%m-%d"),
            "rsi": round(row["RSI_14"], 2)
        },
        axis=1
    ).tolist()

    return rsi_data