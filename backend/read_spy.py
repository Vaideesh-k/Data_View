import psycopg2

# Connect to the local PostgreSQL database
conn = psycopg2.connect(
    dbname="analytics_dashboard",
    user="vaideeshk",
    password="password",
    host="localhost",
    port="5432"
)

# Create a cursor to execute SQL
cur = conn.cursor()

# Query the 'spy' table
try:
    cur.execute('SELECT * FROM spy ORDER BY date DESC LIMIT 10;')
    rows = cur.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

# Clean up
cur.close()
conn.close()