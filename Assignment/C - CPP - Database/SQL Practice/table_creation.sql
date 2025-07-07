create database practice;

use practice;

CREATE TABLE Salespersons (
    SalespersonID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(100)
);

-- Insert 10 Salespersons
INSERT INTO Salespersons (FirstName, LastName, Email) VALUES
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Robert', 'Brown', 'robert.brown@example.com'),
('Emily', 'Davis', 'emily.davis@example.com'),
('Michael', 'Wilson', 'michael.wilson@example.com'),
('Linda', 'Martinez', 'linda.martinez@example.com'),
('David', 'Garcia', 'david.garcia@example.com'),
('Sarah', 'Miller', 'sarah.miller@example.com'),
('James', 'Taylor', 'james.taylor@example.com'),
('Elizabeth', 'Anderson', 'elizabeth.anderson@example.com');


select * from salespersons;

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100),
    SaleDate DATE,
    Amount DECIMAL(10, 2),
    SalespersonID INT,
    FOREIGN KEY (SalespersonID) REFERENCES Salespersons(SalespersonID)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY auto_increment,
    DepartmentName VARCHAR(100) NOT NULL
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY auto_increment,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    HireDate DATE,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY auto_increment,
    ProjectName VARCHAR(100) NOT NULL,
    StartDate DATE,
    EndDate DATE
);

CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    PRIMARY KEY (EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

INSERT INTO Departments (DepartmentName) 
VALUES 
('Human Resources'),
('Engineering'),
('Marketing'),
('Sales'),
('Finance'),
('IT Support'),
('Operations');

INSERT INTO Employees (FirstName, LastName, DepartmentID, HireDate, Salary) 
VALUES 
('John', 'Doe', 2, '2021-03-15', 55000.00),
('Jane', 'Smith', 1, '2020-05-20', 45000.00),
('Alex', 'Johnson', 3, '2019-06-10', 60000.00),
('Emily', 'Davis', 2, '2021-01-05', 62000.00),
('Michael', 'Brown', 4, '2021-09-25', 47000.00),
('Sarah', 'Williams', 5, '2020-04-15', 52000.00),
('David', 'Jones', 6, '2019-07-01', 68000.00),
('Olivia', 'Garcia', 7, '2021-02-10', 59000.00),
('William', 'Miller', 2, '2021-08-12', 54000.00),
('Sophia', 'Taylor', 1, '2020-11-22', 47000.00),
('James', 'Anderson', 3, '2021-03-18', 56000.00),
('Benjamin', 'Thomas', 4, '2020-10-05', 59000.00),
('Charlotte', 'Jackson', 5, '2021-04-19', 51000.00),
('Amelia', 'White', 6, '2021-01-15', 62000.00),
('Lucas', 'Harris', 7, '2020-06-23', 54000.00),
('Mason', 'Clark', 2, '2021-07-09', 59000.00),
('Liam', 'Lewis', 3, '2021-02-14', 63000.00),
('Ethan', 'Young', 4, '2020-05-30', 51000.00),
('Avery', 'Walker', 5, '2021-11-12', 49000.00),
('Harper', 'Allen', 6, '2021-03-10', 65000.00);


INSERT INTO Projects (ProjectName, StartDate, EndDate) 
VALUES 
('Project Alpha', '2021-01-01', '2021-12-31'),
('Project Beta', '2022-03-01', '2022-09-30'),
('Project Gamma', '2021-05-15', '2022-06-30'),
('Project Delta', '2020-06-01', '2020-12-31'),
('Project Epsilon', '2021-07-01', '2022-06-30'),
('Project Zeta', '2021-09-01', '2022-04-30'),
('Project Eta', '2021-10-01', '2022-05-31'),
('Project ECMA', '2020-01-01', '2025-12-31');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID) 
VALUES 
(1, 1),  -- John is working on Project Alpha
(2, 2),  -- Jane is working on Project Beta
(3, 3),  -- Alex is working on Project Gamma
(4, 1),  -- Emily is working on Project Alpha
(5, 4),  -- Michael is working on Project Delta
(6, 5),  -- Sarah is working on Project Epsilon
(7, 6),  -- David is working on Project Zeta
(8, 7),  -- Olivia is working on Project Eta
(9, 1),  -- William is working on Project Alpha
(10, 2), -- Sophia is working on Project Beta
(11, 3), -- James is working on Project Gamma
(12, 4), -- Benjamin is working on Project Delta
(13, 5), -- Charlotte is working on Project Epsilon
(14, 6), -- Amelia is working on Project Zeta
(15, 7), -- Lucas is working on Project Eta
(16, 1), -- Mason is working on Project Alpha
(17, 3), -- Liam is working on Project Gamma
(18, 4), -- Ethan is working on Project Delta
(19, 5), -- Avery is working on Project Epsilon
(20, 6); -- Harper is working on Project Zeta

INSERT INTO Employees (FirstName, LastName, DepartmentID, HireDate, Salary) 
VALUES
('Adam', 'Clark', 2, '2023-04-01', 56000.00),
('Bella', 'Hill', 3, '2023-05-12', 58000.00),
('Charlie', 'Scott', 4, '2023-06-23', 51000.00),
('Diana', 'Harris', 5, '2023-07-10', 54000.00),
('Eli', 'Carter', 6, '2023-08-15', 65000.00),
('Fiona', 'Nelson', 7, '2023-09-03', 57000.00),
('George', 'Kelley', 1, '2023-10-20', 48000.00),
('Hannah', 'Mitchell', 2, '2023-11-10', 50000.00),
('Isaac', 'Young', 3, '2023-12-05', 55000.00),
('Julia', 'Roberts', 4, '2024-01-12', 59000.00),
('Kevin', 'Stewart', 5, '2024-02-01', 51000.00),
('Lily', 'Davis', 6, '2024-03-20', 67000.00),
('Mason', 'Taylor', 7, '2024-04-14', 58000.00),
('Nina', 'Evans', 1, '2024-05-10', 49000.00),
('Oscar', 'Anderson', 2, '2024-06-08', 52000.00),
('Paula', 'Martinez', 3, '2024-07-22', 53000.00),
('Quinn', 'Gonzalez', 4, '2024-08-12', 55000.00),
('Riley', 'King', 5, '2024-09-02', 56000.00),
('Sophie', 'Perez', 6, '2024-10-17', 64000.00),
('Tom', 'Lee', 7, '2024-11-11', 59000.00),
('Uma', 'Walker', 1, '2024-12-25', 50000.00),
('Vera', 'Allen', 2, '2025-01-14', 51000.00),
('Will', 'Wright', 3, '2025-02-10', 53000.00),
('Xander', 'Lopez', 4, '2025-03-07', 55000.00),
('Yara', 'Morris', 5, '2025-04-12', 57000.00),
('Zane', 'Roberts', 6, '2025-05-06', 65000.00),
('Alice', 'Jackson', 7, '2025-06-19', 59000.00),
('Brian', 'Hernandez', 1, '2025-07-13', 48000.00),
('Cora', 'Miller', 2, '2025-08-10', 51000.00),
('Dan', 'Clark', 3, '2025-09-01', 52000.00),
('Elena', 'Lewis', 4, '2025-10-06', 54000.00);

INSERT INTO EmployeeProjects (EmployeeID, ProjectID) 
VALUES 
(21, 1),  -- Adam is working on Project Alpha
(22, 2),  -- Bella is working on Project Beta
(23, 3),  -- Charlie is working on Project Gamma
(24, 4),  -- Diana is working on Project Delta
(25, 5),  -- Eli is working on Project Epsilon
(26, 6),  -- Fiona is working on Project Zeta
(27, 7),  -- George is working on Project Eta
(28, 1),  -- Hannah is working on Project Alpha
(29, 2),  -- Isaac is working on Project Beta
(30, 3),  -- Julia is working on Project Gamma
(31, 4),  -- Kevin is working on Project Delta
(32, 5),  -- Lily is working on Project Epsilon
(33, 6),  -- Mason is working on Project Zeta
(34, 7),  -- Nina is working on Project Eta
(35, 1),  -- Oscar is working on Project Alpha
(36, 2),  -- Paula is working on Project Beta
(37, 3),  -- Quinn is working on Project Gamma
(38, 4),  -- Riley is working on Project Delta
(39, 5),  -- Sophie is working on Project Epsilon
(40, 6),  -- Tom is working on Project Zeta
(41, 7),  -- Uma is working on Project Eta
(42, 1),  -- Vera is working on Project Alpha
(43, 2),  -- Will is working on Project Beta
(44, 3),  -- Xander is working on Project Gamma
(45, 4),  -- Yara is working on Project Delta
(46, 5),  -- Zane is working on Project Epsilon
(47, 6),  -- Alice is working on Project Zeta
(48, 7),  -- Brian is working on Project Eta
(49, 1),  -- Cora is working on Project Alpha
(50, 2);  -- Dan is working on Project Beta

INSERT INTO Sales (ProductName, SaleDate, Amount, SalespersonID) VALUES
('Product A', '2025-04-01', 250.00, 1),
('Product B', '2025-04-02', 300.00, 1),
('Product C', '2025-04-05', 500.00, 2),
('Product D', '2025-04-07', 150.00, 2),
('Product E', '2025-04-10', 200.00, 3),
('Product F', '2025-04-12', 400.00, 3),
('Product G', '2025-04-14', 450.00, 3),
('Product H', '2025-04-17', 150.00, 4),
('Product I', '2025-04-20', 300.00, 4),
('Laptop', '2025-04-01', 2200.00, 1),
('Smartphone', '2025-04-02', 950.00, 2),
('Headphones', '2025-04-05', 150.00, 3),
('Smartwatch', '2025-04-07', 200.00, 4),
('Tablet', '2025-04-10', 500.00, 5),
('Keyboard', '2025-04-12', 50.00, 6),
('Mouse', '2025-04-15', 30.00, 7),
('Monitor', '2025-04-17', 250.00, 8),
('Router', '2025-04-20', 120.00, 9),
('Camera', '2025-04-22', 800.00, 10),
('Speaker', '2025-04-24', 150.00, 1),
('Printer', '2025-04-26', 100.00, 2),
('External Hard Drive', '2025-04-29', 80.00, 3),
('USB Flash Drive', '2025-04-30', 15.00, 4),
('Game Console', '2025-05-02', 350.00, 5),
('Digital Camera', '2025-05-04', 700.00, 6),
('Air Purifier', '2025-05-06', 150.00, 7),
('Coffee Maker', '2025-05-08', 120.00, 8),
('Blender', '2025-05-10', 80.00, 9),
('Microwave', '2025-05-12', 200.00, 10),
('Dishwasher', '2025-05-14', 400.00, 1),
('Vacuum Cleaner', '2025-05-16', 150.00, 2),
('Air Conditioner', '2025-05-18', 600.00, 3),
('Refrigerator', '2025-05-20', 1200.00, 4),
('Washing Machine', '2025-05-22', 800.00, 5),
('Electric Kettle', '2025-05-24', 40.00, 6),
('Treadmill', '2025-05-26', 500.00, 7),
('Electric Toothbrush', '2025-05-28', 70.00, 8),
('Blender', '2025-05-30', 130.00, 9),
('Smart Light Bulb', '2025-06-01', 20.00, 10),
('Coffee Grinder', '2025-06-03', 30.00, 1),
('Stand Mixer', '2025-06-05', 150.00, 2),
('Cordless Drill', '2025-06-07', 100.00, 3),
('Electric Grill', '2025-06-09', 70.00, 4),
('Toaster', '2025-06-11', 40.00, 5),
('Food Processor', '2025-06-13', 120.00, 6),
('Pressure Cooker', '2025-06-15', 90.00, 7),
('Lawn Mower', '2025-06-17', 200.00, 8),
('Sewing Machine', '2025-06-19', 150.00, 9);
