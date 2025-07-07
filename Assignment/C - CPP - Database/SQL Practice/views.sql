-- -> Why Use Views:

-- Complex query ko reusable banana
CREATE VIEW basic_employees_info as 
	select e.employeeid, e.firstname, e.lastname, d.departmentname, p.projectname
	from employees e join departments d on e.departmentid = d.departmentid
	join employeeprojects ep on e.employeeid = ep.EmployeeID
	join projects p on ep.ProjectID = p.ProjectID 
	order by employeeid;

select * from basic_employees_info;


-- Data ko filter/secure karke show karna
CREATE VIEW PublicEmployeeList AS
SELECT EmployeeID, FirstName, LastName, DepartmentID
FROM Employees;

select * from PublicEmployeeList;


-- Code readability improve karna
CREATE VIEW DepartmentStats AS
SELECT DepartmentID, COUNT(*) AS TotalEmployees, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentID;

SELECT * FROM DepartmentStats WHERE DepartmentID = 3;


-- Extra:
create view getMarketingEmployees as  select * from employees where DepartmentID = 3;

select * from getMarketingEmployees;

drop view employeesWithoutProject;

create view employeesWithoutProject as  
	select e.employeeid, e.firstname, e.lastname, e.salary 
    from employees e left join employeeprojects ep 
    on e.EmployeeID = ep.EmployeeID 
    where ep.EmployeeID is null order by EmployeeID;

select * from employeesWithoutProject where salary > 80000;

















