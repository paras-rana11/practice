import mysql.connector
import random

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root1',
    database='healthcare'
)
cursor = conn.cursor()

# Step 1: Get all distinct doctor_ids
cursor.execute("SELECT doctor_id FROM doctors")
doctor_ids = [row[0] for row in cursor.fetchall()]

# Step 2: Get all patient_visit ids
cursor.execute("SELECT visit_id FROM patient_visits")
visit_ids = [row[0] for row in cursor.fetchall()]
random.shuffle(visit_ids)

# Step 3: Distribute visit_ids to doctors with varying load
index = 0
for doctor_id in doctor_ids:
    visit_chunk_size = random.randint(40, 300)  # Each doctor gets 50–200 visits
    visit_chunk = visit_ids[index:index + visit_chunk_size]
    if not visit_chunk:
        break
    format_strings = ','.join(['%s'] * len(visit_chunk))
    query = f"""
        UPDATE patient_visits
        SET doctor_id = %s
        WHERE visit_id IN ({format_strings})
    """
    cursor.execute(query, (doctor_id, *visit_chunk))
    index += visit_chunk_size

conn.commit()
cursor.close()
conn.close()
print("✅ Updated existing patient_visits to vary doctor visit counts.")
