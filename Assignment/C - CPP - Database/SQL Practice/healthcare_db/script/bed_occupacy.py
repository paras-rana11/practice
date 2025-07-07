import mysql.connector
import random

# 🔧 MySQL Configuration
config = {
    'host': 'localhost',
    'user': 'root',         # update this
    'password': 'root1', # update this
    'database': 'healthcare'  # update this
}

# 🔌 Connect to database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

try:
    # Reset all beds
    print("Resetting all bed_occupied to 0...")
    cursor.execute("UPDATE patient_visits SET bed_occupied = 0;")
    conn.commit()

    # Get department IDs
    cursor.execute("SELECT dept_id FROM departments;")
    dept_ids = [row[0] for row in cursor.fetchall()]

    # Update each department
    for dept_id in dept_ids:
        occupancy_percent = random.randint(20, 90) / 100

        # Step 1: count rows in department
        cursor.execute(f"SELECT COUNT(*) FROM patient_visits WHERE department_id = {dept_id};")
        total = cursor.fetchone()[0]
        limit = int(round(total * occupancy_percent))

        print(f"Updating dept_id {dept_id} with {limit}/{total} occupied beds (~{int(occupancy_percent*100)}%)")

        # Step 2: apply occupancy
        if limit > 0:
            cursor.execute(f"""
                UPDATE patient_visits
                SET bed_occupied = 1
                WHERE department_id = {dept_id}
                ORDER BY RAND()
                LIMIT {limit};
            """)
            conn.commit()

    print("✅ Occupancy updated for all departments.")

except Exception as e:
    print("❌ Error:", e)

finally:
    cursor.close()
    conn.close()
