import psycopg2
import numpy as np

def get_daily_close_change():
    conn = psycopg2.connect(
        dbname="analytics_dashboard",
        user="vaideeshk",
        password="password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Get all close prices ordered by date
    cur.execute("SELECT date, close FROM spy ORDER BY date ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Extract dates and close prices
    dates = [row[0] for row in rows]
    closes = [float(row[1]) for row in rows]

    # Compute daily differences
    diff_array = np.diff(closes)

    # Build result as list of dicts, skipping the first date (no diff)
    result = [
        {
            "date": dates[i + 1].strftime("%Y-%m-%d"),
            "daily_change": round(change, 2)
        }
        for i, change in enumerate(diff_array)
    ]

    return result