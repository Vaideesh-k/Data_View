import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the database
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM spy ORDER BY timestamp DESC LIMIT 10;")

# Fetch and print rows
rows = cur.fetchall()
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()