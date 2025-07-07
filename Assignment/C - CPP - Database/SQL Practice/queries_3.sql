create database test;
use test;

-- Q1.
--  Write an SQL query to create a table employees with columns: id (Primary Key), name (VARCHAR), salary (INT), and department (VARCHAR).
create table Employees(
	EmployeeID int primary key auto_increment,
    EmployeeName varchar(50) unique,
    Salary int,
    Department varchar(50));

drop tables employees;

-- Q2.
--  Write an SQL query to insert three employee records into the employees table.
INSERT INTO Employees (employeename, salary, department) VALUES
('Tanjiro Kamado', 55000, 'HR'),
('Inosuke Hashibira', 35000, 'Accounting'),
('Zenitsu Agatsuma', 70000, 'IT'),
('Nezuko Kamado', 60000, 'Sales'),
('Kanao Tsuyuri', 45000, 'Sales'),
('Tengen Uzui', 75000, 'Customer Support'),
('Mitsuri Kanroji', 72000, 'Engineering'),
('Shinobu Kocho', 68000, 'CEO'),
('Rengoku Kyojuro', 80000, 'Operations'),
('Giyu Tomioka', 55000, 'IT'),
('Muichiro Tokito', 48000, 'HR'),
('Sanemi Shinazugawa', 49000, 'Operations'),
('Obanai Iguro', 60000, 'Customer Support'),
('Kagaya Ubuyashiki', 95000, 'Sales'),
('Yoriichi Tsugikuni', 85000, 'Sales'),
('Kibutsuji Muzan', 120000, 'CEO');

select * from employees;
truncate employees;

-- Q3. 
--  Write an SQL query to update the salary of employees in the "Sales" department by 10%.
SET SQL_SAFE_UPDATES = 0;

update employees set salary = (salary + salary*0.10) where department = 'sales';


-- Q4.
--  Write an SQL query to select all departments where the average salary is greater than 50,000. Group the results accordingly and order by average salary in descending order.

-- Q5.
--  Write SQL queries for:
-- a) Dropping the employees table.


-- b) Granting SELECT permission on a products table to user john.


-- c) Revoking INSERT permission on a products table from user john.




-- Q6.
-- You have two tables:
-- students(id, name, class_id)  
-- classes(id, class_name)
-- Write an SQL query to fetch a list of students along with their class name using a JOIN.
