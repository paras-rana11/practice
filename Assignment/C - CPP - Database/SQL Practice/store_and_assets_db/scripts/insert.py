import mysql.connector
from faker import Faker
import random
import datetime

# Create a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",        # For example, localhost
    user="root",             # Your MySQL username
    password="root1",        # Your MySQL password
    database="hospital_store_and_assets" # Your database name
)

cursor = db.cursor()

# Initialize Faker to generate random data
fake = Faker()

# Number of entries to generate
num_entries = 1000

# Function to insert categories
def insert_categories():
    categories = [
        ("Medical Supplies", "Items needed for day-to-day medical treatments."),
        ("Medical Equipment", "Machines and equipment used for diagnostics and treatment."),
        ("Hospital Assets", "Long-term assets used across the hospital."),
        ("Pharmaceuticals", "Drugs and medicinal substances used in patient care."),
        ("Laboratory Supplies", "Tools and materials used for laboratory testing."),
        ("Diagnostic Equipment", "Machines used for diagnostic purposes, such as MRI, X-ray, etc."),
        ("Surgical Instruments", "Tools used in surgeries, including scalpels, forceps, etc."),
        ("Consumables", "Single-use items that are consumed during medical procedures."),
        ("Healthcare Furniture", "Beds, chairs, and other furniture used in healthcare settings."),
        ("Personal Protective Equipment", "Items like gloves, masks, and gowns used to ensure safety."),
    ]
    
    category_data = []
    for category_name, description in categories:
        category_data.append((category_name, description))
    
    cursor.executemany("INSERT INTO categories (category_name, description) VALUES (%s, %s)", category_data)
    db.commit()

# Function to insert items
def insert_items():
    item_names = [
        "Syringe", "Bandage", "Stethoscope", "Wheelchair", "X-Ray Machine", "CT Scanner", 
        "IV Drip", "Blood Pressure Monitor", "Thermometer", "Scalpel", "Forceps", "Sutures", 
        "Pulse Oximeter", "Fetal Monitor", "ECG Machine", "Defibrillator", "Ambulance Stretcher", 
        "Oxygen Tank", "Surgical Gloves", "Oxygen Mask", "Surgical Gown", "Microscope", "Test Tubes", 
        "Beakers", "Electrocardiograph", "Surgical Blade", "Infusion Pump", "Hearing Aid", 
        "Diabetes Testing Kit", "Dialysis Machine", "Ventilator"
    ]
    item_types = ["Medical Supply", "Medical Equipment", "Asset"]
    units = ["pcs", "each", "set", "unit"]
    
    item_data = []
    
    for _ in range(num_entries):
        category_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        item_name = random.choice(item_names)
        item_code = fake.uuid4()
        item_type = random.choice(item_types)
        unit_of_measure = random.choice(units)

        if item_type == "Medical Supply":
            price = random.uniform(1, 100)
        elif item_type == "Medical Equipment":
            price = random.uniform(500, 5000)
        else:
            price = random.uniform(1000, 20000)

        item_data.append((item_code, item_name, fake.text(), category_id, unit_of_measure, item_type))
    
    cursor.executemany("INSERT INTO items (item_code, name, description, category_id, unit_of_measure, item_type) VALUES (%s, %s, %s, %s, %s, %s)", item_data)
    db.commit()

# Function to insert departments
def insert_departments():
    store_types = ['Main Department', 'Sub Department', 'Specialized Ward']
    department_names = [
        "Cardiology", "Neurology", "Orthopedics", "General Medicine", "Radiology", "Emergency", 
        "Pediatrics", "Surgery", "Intensive Care Unit (ICU)", "Neonatal ICU", "Burn Unit", "Psychiatry", 
        "Oncology", "Laboratory", "Pharmacy", "Geriatrics", "Physical Therapy", "Pulmonology", 
        "Rheumatology", "Urology"
    ]
    
    store_data = []
    
    for _ in range(num_entries):
        store_name = random.choice(department_names)  # Hospital department/ward name
        location = fake.address()  # Hospital department/ward location
        store_type = random.choices(store_types, weights=[50, 30, 20], k=1)[0]  # Skew towards main departments
        store_data.append((store_name, location, store_type))
    
    cursor.executemany("INSERT INTO stores (store_name, location, store_type) VALUES (%s, %s, %s)", store_data)
    db.commit()

# Function to insert suppliers
def insert_suppliers():
    supplier_names = [
        "MedTech Supplies", "Global Healthcare", "Hospital Supplies Inc.", "CarePlus Medical", "Healthcare Supplies Ltd."
    ]
    
    supplier_data = []
    
    for _ in range(num_entries):
        name = random.choice(supplier_names)
        contact_info = fake.phone_number()
        supplier_data.append((name, contact_info))
    
    cursor.executemany("INSERT INTO suppliers (name, contact_info) VALUES (%s, %s)", supplier_data)
    db.commit()

# Function to insert inventory stock
def insert_inventory_stock():
    inventory_data = []
    
    for _ in range(num_entries):
        item_id = random.randint(1, 1000)
        store_id = random.randint(1, 1000)
        
        # Retrieve item type for the current item_id
        cursor.execute("SELECT item_type FROM items WHERE item_id = %s", (item_id,))
        item_type_result = cursor.fetchone()
        
        if item_type_result:
            item_type = item_type_result[0]  # Extract the item_type from the result
        else:
            continue
        
        # Skew towards high stock for supplies, lower stock for equipment
        if item_type == "Medical Supply":
            quantity = random.gauss(1000, 500)
        elif item_type == "Medical Equipment":
            quantity = random.gauss(50, 20)
        else:
            quantity = random.gauss(100, 50)

        quantity = max(0, quantity)

        inventory_data.append((item_id, store_id, quantity))

    if inventory_data:
        cursor.executemany("INSERT INTO inventory_stock (item_id, store_id, quantity) VALUES (%s, %s, %s)", inventory_data)
        db.commit()

# Function to insert purchase orders
def insert_purchase_orders():
    purchase_order_data = []
    
    for _ in range(num_entries):
        supplier_id = random.randint(1, 1000)
        order_date = fake.date_this_year()
        expected_delivery = fake.date_this_year()

        purchase_order_data.append((supplier_id, order_date, expected_delivery))
    
    if purchase_order_data:
        cursor.executemany("INSERT INTO purchase_orders (supplier_id, order_date, expected_delivery) VALUES (%s, %s, %s)", purchase_order_data)
        db.commit()

# Function to insert purchase order items
def insert_purchase_order_items():
    po_item_data = []
    
    for _ in range(num_entries):  
        po_id = random.randint(1, 1000)  # Random purchase order id
        item_id = random.randint(1, 1000)  # Random item id
        quantity = random.uniform(1, 100)  # Random quantity for the item
        unit_price = random.uniform(10, 500)  # Random unit price for the item
        
        po_item_data.append((po_id, item_id, quantity, unit_price))
    
    if po_item_data:
        cursor.executemany("INSERT INTO purchase_order_items (po_id, item_id, quantity, unit_price) VALUES (%s, %s, %s, %s)", po_item_data)
        db.commit()

# Function to insert users
def insert_users():
    user_data = []
    
    # Generate random users (you can adjust the fields according to your schema)
    for _ in range(num_entries):
        name = fake.name()  # Adjusting field to match database schema
        designation = random.choice(['Doctor', 'Nurse', 'Technician', 'Pharmacist', 'Admin'])  # Add roles as needed
        department = random.choice(['Cardiology', 'Neurology', 'Orthopedics', 'General Medicine', 'Radiology'])  # Random departments
        email = fake.email()
        
        # Add a new user to the list
        user_data.append((name, designation, department, email))
    
    # Insert users into the 'users' table
    cursor.executemany("INSERT INTO users (name, designation, department, email) VALUES (%s, %s, %s, %s)", user_data)
    db.commit()
    print(f"Inserted {num_entries} users.")

# Function to insert asset register data
def insert_asset_register():
    asset_data = []
    
    for _ in range(num_entries):
        item_id = random.randint(1, 1000)
        serial_number = fake.uuid4()
        purchase_date = fake.date_this_year()
        location_id = random.randint(1, 1000)
        assigned_to = random.randint(1, 1000)
        status = random.choice(['In Use', 'In Maintenance', 'Disposed'])
        value = random.uniform(1000, 20000)
        depreciation_rate = random.uniform(5, 20)
        useful_life_years = random.randint(1, 10)
        
        asset_data.append((item_id, serial_number, purchase_date, location_id, assigned_to, status, value, depreciation_rate, useful_life_years))
    
    cursor.executemany("INSERT INTO asset_register (item_id, serial_number, purchase_date, location_id, assigned_to, status, value, depreciation_rate, useful_life_years) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", asset_data)
    db.commit()

# Function to insert asset maintenance data
def insert_asset_maintenance():
    maintenance_data = []
    
    for _ in range(num_entries):
        asset_id = random.randint(1, 1000)
        maintenance_date = fake.date_this_year()
        description = fake.text()
        cost = random.uniform(50, 2000)
        performed_by = fake.name()
        next_due_date = fake.date_this_year()
        
        maintenance_data.append((asset_id, maintenance_date, description, cost, performed_by, next_due_date))
    
    cursor.executemany("INSERT INTO asset_maintenance (asset_id, maintenance_date, description, cost, performed_by, next_due_date) VALUES (%s, %s, %s, %s, %s, %s)", maintenance_data)
    db.commit()

# Function to insert transactions (movement of items)
def insert_transactions():
    transaction_data = []
    
    for _ in range(num_entries):
        item_id = random.randint(1, 1000)
        transaction_type = random.choice(['Issue', 'Receive', 'Transfer'])
        quantity = random.uniform(1, 100)
        store_id = random.randint(1, 1000)
        transaction_date = fake.date_this_year()
        reference_no = fake.uuid4()
        performed_by = fake.name()
        
        transaction_data.append((item_id, transaction_type, quantity, store_id, transaction_date, reference_no, performed_by))
    
    cursor.executemany("INSERT INTO transactions (item_id, transaction_type, quantity, store_id, transaction_date, reference_no, performed_by) VALUES (%s, %s, %s, %s, %s, %s, %s)", transaction_data)
    db.commit()

# Function to insert asset disposal data
def insert_asset_disposal():
    disposal_data = []
    
    for _ in range(num_entries):
        asset_id = random.randint(1, 1000)
        disposal_date = fake.date_this_year()
        method = random.choice(['Sold', 'Scrapped', 'Donated'])
        value_recovered = random.uniform(100, 2000)
        remarks = fake.text()
        
        disposal_data.append((asset_id, disposal_date, method, value_recovered, remarks))
    
    cursor.executemany("INSERT INTO asset_disposal (asset_id, disposal_date, method, value_recovered, remarks) VALUES (%s, %s, %s, %s, %s)", disposal_data)
    db.commit()

# Final function to call all insert functions sequentially
def insert_all_data():
    try:
        db.start_transaction()
        
        # Insert data in the correct order:
        insert_users()
        # insert_categories()
        insert_items()
        insert_departments()
        insert_suppliers()
        insert_inventory_stock()
        insert_purchase_orders()
        insert_purchase_order_items()
        insert_asset_register()
        insert_asset_maintenance()
        insert_transactions()
        insert_asset_disposal()
        
        db.commit()
        print("Data insertion complete.")
    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error: {err}")

# Call the function to insert data
insert_all_data()
