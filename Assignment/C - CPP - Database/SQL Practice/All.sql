select * from employees;

show tables;
show full tables where table_type='BASE TABLE';
show full tables where table_type='VIEW';


SELECT COUNT(*) FROM employees;

select * from employees limit 3 offset 17;   -- (total rows - limit = offset), (here, 20 - 3 = 17)

select DepartmentID, min(salary) from employees group by DepartmentID;

SELECT d.DepartmentName, MIN(e.salary) AS minimum_salary
FROM employees e
JOIN departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

SELECT d.DepartmentName, e.EmployeeID, e.FirstName, e.salary
FROM employees e
JOIN departments d ON e.DepartmentID = d.DepartmentID
WHERE e.salary = (
    SELECT MIN(e1.salary)
    FROM employees e1
    WHERE e1.DepartmentID = e.DepartmentID
)
ORDER BY d.DepartmentName;

select concat(firstname, ' ', lastname) as Full_Name from employees;

select avg(salary) from employees;

select e.EmployeeID, e.firstname, p.projectname from employees e
join employeeprojects ep on e.EmployeeID = ep.EmployeeID
join projects p on ep.ProjectID=p.ProjectID
order by e.EmployeeID;

-- SELF JOIN
SELECT 
    e1.FirstName AS EmployeeName, 
    e1.LastName AS EmployeeLastName, 
    e2.FirstName AS ColleagueName,
    e2.LastName AS ColleagueLastName,
    e1.DepartmentID AS DepartmentID
FROM 
    Employees e1
JOIN 
    Employees e2 ON e1.DepartmentID = e2.DepartmentID 
WHERE 
    e1.EmployeeID != e2.EmployeeID
ORDER BY 
    e1.DepartmentID;

-- union gives unique data, union all gives all data:
select firstname as fname from employees union all select DepartmentName as dept from departments;

select count(employeeid) from employees;

select departmentID , count(employeeid) as emp_in_dept from employees group by departmentid;

select d.departmentname, count(e.employeeid) as emp_in_dept 
from employees e
join departments d on e.DepartmentID = d.DepartmentID
group by e.departmentid;

select d.departmentname as dept_name, sum(e.salary) as dept_vise_salary
from employees e
join departments d on e.DepartmentID=d.DepartmentID
group by DepartmentName;

select d.departmentname , sum(e.salary) 
from employees e 
join departments d on e.DepartmentID = d.DepartmentID 
group by departmentname 
having sum(e.salary) < 450000 ;


select d.departmentname, count(e.employeeid) from employees e join departments d on e.DepartmentID=d.DepartmentID
group by DepartmentName
having count(e.EmployeeID) > 6 order by DepartmentName desc;

SELECT FirstName, LastName
FROM employees
WHERE Salary > ALL (SELECT Salary FROM employees WHERE DepartmentID = 3);

create table tbd as select * from employees;
truncate tbd;
insert into tbd select * from employees where firstname like 'j%' or firstname like 'c%';
select *  from tbd;
drop table tbd;


SELECT firstname, lastname, salary
FROM employees
ORDER BY
(CASE
    WHEN salary <= 50000 THEN 1
    WHEN salary > 50000 and salary <= 60000 THEN 2
    WHEN salary > 60000 and salary <= 70000 THEN 3
    WHEN salary > 70000 and salary <= 80000 THEN 4
    ELSE 0
END);


select date(startdate) from projects;

select startdate from projects;

select * from departments;

create view Sales_Department as select * from employees where departmentid = 4;

select * from sales_Department;

create view HR_Department as select * from employees where departmentid = 1;

select * from HR_Department;

create view dept_vise_min_salary as
SELECT d.DepartmentName, MIN(e.salary) AS minimum_salary
FROM employees e
JOIN departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

select * from dept_vise_min_salary;


-- PROCEDURES: 
delimiter !!
	create procedure getEmployeeDetails(in emp_id int)
    begin
		select * from employees where employeeid = emp_id;
    end !!
delimiter ;

call getEmployeeDetails(11);

delimiter !! 
	create procedure getDepartmentName(in dept_id int)
	begin
		select departmentname from departments where DepartmentID=dept_id;
	end !! 
delimiter ;

call getDepartmentname(7);



select p.projectname, e.employeeid, e.firstname 
from employees e
join employeeprojects ep on e.employeeid = ep.employeeid
left join projects p on p.projectid = ep.projectid
order by projectname;


delimiter !!
	create procedure getProjectEmployees(in  project_id int)
	begin
		select e.employeeid, e.firstname, p.projectname 
		from employees e
		join employeeprojects ep on e.employeeid = ep.employeeid
		left join projects p on p.projectid = ep.projectid
		where p.projectid = project_id;
	end !!
delimiter ;

call getProjectEmployees(7);


delimiter !!
	create procedure updateSalary(in e_id int, in new_salary decimal(10,2))
	begin
		update employees set salary = new_salary where employeeid = e_id;
        
        select * from employees where employeeid = e_id;
	end !!
delimiter ;

select * from employees where employeeid = 1;

call updateSalary(1, 70000);

-- FUNCTIONS:

DELIMITER !!
	CREATE FUNCTION getFullName(first_name varchar(50), last_name varchar(50))
    RETURNS varchar(50)
    DETERMINISTIC
    
    BEGIN
		RETURN CONCAT(first_name, ' ', last_name);
    END !!
DELIMITER ;

select getFullName(firstname, lastname) from employees;


DELIMITER !! 
	create function getAvgSalaryFromDepartment(dept_id int)
    returns int
    deterministic
    BEGIN
		declare avg_salary int;
    
		select avg(e.salary) into avg_salary
		from employees e
		join departments d on e.DepartmentID = d.DepartmentID
        where d.departmentid = dept_id;
        
        return avg_salary;
    END !!
DELIMITER ;

drop function getAvgSalaryFromDepartment;

select departmentname, getAvgSalaryFromDepartment(1) from departments where departmentid = 1;


select d.departmentname, avg(e.salary)
from employees e
join departments d on e.DepartmentID = d.DepartmentID
group by DepartmentName;


create table salary_changes (Sr_no int primary key auto_increment, e_id int, e_fullname varchar(100), old_salary int, new_salary int, date_time datetime);

drop table salary_changes;

DELIMITER $$

CREATE TRIGGER afterUpdateSalary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    -- Check if the salary has actually changed
    IF OLD.salary <> NEW.salary THEN
        -- Insert a record into salary_changes table when salary changes
        INSERT INTO salary_changes (e_id, e_fullname, old_salary, new_salary, date_time)
        VALUES (
            OLD.employeeid, 
            CONCAT(IFNULL(OLD.firstname, ''), ' ', IFNULL(OLD.lastname, '')),  -- Handle NULL values
            OLD.salary, 
            NEW.salary, 
            NOW()
        );
    END IF;
END$$

DELIMITER ;

drop trigger afterUpdateSalary;


call updateSalary(51, 65000);

select * from salary_changes;

create view getEmployeesProjectVise as
select count(e.employeeid), p.projectname 
from employees e
join employeeprojects ep on e.employeeid = ep.employeeid
join projects p on ep.projectid = p.projectid
group by p.projectname;


select * from getEmployeesProjectVise;

SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e
LEFT JOIN EmployeeProjects ep ON e.EmployeeID = ep.EmployeeID
WHERE ep.ProjectID IS NULL;

delimiter !!
	create procedure updateDepartment(in e_id int, in new_dept_id int)
	begin
		
		if exists (select 1 from employees where employeeid = e_id)  then
			if (select 1 from departments where departmentid = new_dept_id ) then
				update employees set departmentid = new_dept_id where employeeid = e_id;
            
				select * from employees where EmployeeID = e_id;
			else
				select "Enter Valid Department ID" as message;
            end if;
		else
			select 'Enter Valid Employee ID' AS message;
        end if;
    end !!
delimiter ;
drop procedure updateDepartment;
call updateDepartment(91, 9);

 select * from employees where EmployeeID = 1;


delimiter !!
	create function getProjectName(e_id int)
	returns varchar(50)
    deterministic
	begin
        declare projectName varchar(50);
        
		select p.projectname into projectName from projects p
        join employeeprojects ep on p.ProjectID = ep.ProjectID
        join employees e on ep.EmployeeID = e.EmployeeID
        where e.EmployeeID = e_id;
        
        return projectName;
    end !!
delimiter ;


select *, getProjectName(1) as projectName from employees where EmployeeID = 1;

create table dept_changes (Sr_no int primary key auto_increment, e_id int, old_dept_id int, old_dept_name varchar(50), new_dept_id int, new_dept_name varchar(50), date_time datetime);
desc dept_changes;

delimiter !!
	create trigger afterUpdateDepartment
    after update on employees
    for each row
	begin
		declare old_deptName varchar(50);
        declare new_deptName varchar(50);
        
        select departmentname into old_deptName from departments where departmentid = old.DepartmentID; 
        select departmentname into new_deptName from departments where departmentid = new.DepartmentID;
        
        if old.DepartmentID <> new.DepartmentID then
			insert into dept_changes (e_id, old_dept_id, old_dept_name, new_dept_id, new_dept_name, date_time) 
					values ( old.employeeid, old.departmentid, old_deptName, new.DepartmentID, new_deptName, now() );
		end if;
    end !!
delimiter ;

drop trigger afterUpdateDepartment;

call updateDepartment(1, 5);

select * from dept_changes;
























































































