select * from employees;

delimiter //
	create procedure getTotalEmployeesInDepartment (in dept_id int)
    begin
		select d.departmentname, count(e.employeeid) as Total_Employees_In_Department
        from departments d join employees e 
        on d.DepartmentID = e.DepartmentID
        group by e.DepartmentID having e.DepartmentID = dept_id;
	end //

delimiter ;

drop procedure getEmployeesWithoutProject;

delimiter !!
	create procedure getEmployeesWithoutProject()
	begin
		select e.employeeid, e.firstname, e.lastname from employees e left join employeeprojects ep on e.employeeid = ep.employeeid where ep.employeeid is null order by e.employeeid;
    end !!
delimiter ;

call getEmployeesWithoutProject();

call getTotalEmployeesInDepartment(2);

call getProjectEmployees(21);








