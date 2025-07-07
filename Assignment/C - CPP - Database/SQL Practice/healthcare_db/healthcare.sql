-- Create the database
CREATE DATABASE IF NOT EXISTS healthcare;
USE healthcare;

DROP DATABASE healthcare;


-- Create departments table
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) UNIQUE NOT NULL
);

-- Create doctors table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    specialization VARCHAR(100),
    doctor_type ENUM('local', 'foreign') NOT NULL,
    country_of_origin VARCHAR(100),
    license_number VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Create patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    patient_type ENUM('local', 'foreign') NOT NULL,
    country_of_origin VARCHAR(100)
);

-- Create diseases table
CREATE TABLE diseases (
    disease_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_name VARCHAR(100) UNIQUE NOT NULL
);

alter table diseases add column created_at date;

update diseases set created_at = '2020-02-02' where disease_id = 11;

update diseases set created_at = '2021-11-20' where disease_id = 10;

-- Create patient_visits table
CREATE TABLE patient_visits (
    visit_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    department_id INT,
    disease_id INT,
    visit_date DATE NOT NULL,
    bed_occupied TINYINT(1),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (department_id) REFERENCES departments(dept_id),
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);



