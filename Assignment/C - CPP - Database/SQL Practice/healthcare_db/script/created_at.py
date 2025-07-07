import random
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="healthcare"
)
cursor = conn.cursor()

# Weighted years — more weight to 2020
years = [2020]*4 + [2021]*2 + [2022]*2 + [2023]*3 + [2024]*7

# Function to generate random date within a year
def random_date_in_year(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

# Fetch all diseases
cursor.execute("SELECT disease_id FROM diseases")
diseases = cursor.fetchall()

# Update each disease with weighted random date
for (disease_id,) in diseases:
    year = random.choice(years)
    created_at = random_date_in_year(year)
    cursor.execute("""
        UPDATE diseases
        SET created_at = %s
        WHERE disease_id = %s
    """, (created_at.strftime('%Y-%m-%d'), disease_id))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Diseases created_at updated with weighted random years (2020 favored).")
