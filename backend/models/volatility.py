import psycopg2
import numpy as np

def get_volatility_data():
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT date, high, low FROM spy ORDER BY date ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Compute volatility = high - low
    result = []
    for row in rows:
        date, high, low = row
        volatility = round(float(high) - float(low), 4)
        result.append({
            "date": date.strftime("%Y-%m-%d"),
            "volatility": volatility
        })

    return result