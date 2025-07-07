CREATE DATABASE company_db;

drop database company_db;

CREATE DATABASE IF NOT EXISTS company_db;

USE company_db;

-- Departments Table
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(255) NOT NULL
);

-- Projects Table
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Employees Table
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    position VARCHAR(50),
    gender VARCHAR(10),
    date_of_birth DATE,
    dept_id INT,
    project_id INT,
    hire_date DATE,
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

ALTER TABLE employees MODIFY COLUMN phone_number VARCHAR(20);


select * from projects;

select d.*, p.* from departments d  left join projects p on p.dept_id = d.dept_id;-- where p.dept_id is null;
