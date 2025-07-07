-- Create Database for Hospital Store and Asset Management System
CREATE DATABASE hospital_store_and_assets;

USE hospital_store_and_assets;

DROP DATABASE hospital_store_and_assets;

-- Table: categories (Replaced with Hospital-related categories)
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Table: items (Medical supplies, Equipment, and Assets)
CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT,
    unit_of_measure VARCHAR(20),
    item_type ENUM('Medical Supply', 'Medical Equipment', 'Asset') NOT NULL,
    reorder_level INT DEFAULT 0,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Table: stores (Replaced "store" with "department" or "ward" for hospital context)
CREATE TABLE stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,       -- Example: "Emergency Ward", "ICU"
    location TEXT,                          -- Example: "2nd Floor, Building A"
    store_type ENUM('Main Department', 'Sub Department', 'Specialized Ward')  -- "Main Department" could be "General Medicine", "ICU", etc.
);

-- Table: inventory_stock (Manage stock in different departments/wards)
CREATE TABLE inventory_stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    store_id INT,
    quantity DECIMAL(10,2) DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Table: suppliers (Suppliers for medical equipment and supplies)
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info TEXT
);

-- Table: purchase_orders (Purchase orders for medical supplies and equipment)
CREATE TABLE purchase_orders (
    po_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT,
    order_date DATE,
    expected_delivery DATE,
    status ENUM('Pending', 'Received', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Table: purchase_order_items (Items in the purchase orders)
CREATE TABLE purchase_order_items (
    poi_id INT AUTO_INCREMENT PRIMARY KEY,
    po_id INT,
    item_id INT,
    quantity DECIMAL(10,2),
    unit_price DECIMAL(10,2),
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

-- Table: users (Hospital staff including doctors, nurses, technicians, etc.)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    designation VARCHAR(100),  -- Example: "Doctor", "Nurse", "Technician"
    department VARCHAR(100),   -- Example: "Cardiology", "Neurology"
    email VARCHAR(100)
);

-- Table: asset_register (Medical equipment and hospital assets)
CREATE TABLE asset_register (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    serial_number VARCHAR(100),
    purchase_date DATE,
    location_id INT,             -- Refers to store/department where the asset is located
    assigned_to INT,             -- User (e.g., a doctor or department head responsible for the asset)
    status ENUM('In Use', 'In Maintenance', 'Disposed'),
    value DECIMAL(10,2),
    depreciation_rate DECIMAL(5,2),
    useful_life_years INT,
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (location_id) REFERENCES stores(store_id),
    FOREIGN KEY (assigned_to) REFERENCES users(user_id)
);

-- Table: asset_maintenance (Maintenance history for medical equipment)
CREATE TABLE asset_maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    maintenance_date DATE,
    description TEXT,
    cost DECIMAL(10,2),
    performed_by VARCHAR(100),
    next_due_date DATE,
    FOREIGN KEY (asset_id) REFERENCES asset_register(asset_id)
);

-- Table: transactions (Movement of medical supplies or equipment between departments)
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    transaction_type ENUM('Issue', 'Receive', 'Transfer'),
    quantity DECIMAL(10,2),
    store_id INT,                -- Store/department where the transaction happens
    transaction_date DATE,
    reference_no VARCHAR(100),
    performed_by VARCHAR(100),   -- Staff member performing the transaction
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Table: asset_disposal (Disposal of medical equipment)
CREATE TABLE asset_disposal (
    disposal_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    disposal_date DATE,
    method ENUM('Sold', 'Scrapped', 'Donated'),
    value_recovered DECIMAL(10,2),
    remarks TEXT,
    FOREIGN KEY (asset_id) REFERENCES asset_register(asset_id)
);


-- Average price per item (assuming purchase_order_items has price data)
CREATE OR REPLACE VIEW avg_item_prices AS
SELECT
    item_id,
    AVG(unit_price) AS avg_unit_price
FROM
    purchase_order_items
GROUP BY item_id;

