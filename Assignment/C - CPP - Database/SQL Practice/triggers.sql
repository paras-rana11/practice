
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



create table project_changes (Sr_no int primary key auto_increment, e_id int, e_fullname varchar(100), old_project int, new_project int, date_time datetime);


delimiter !!
	create trigger afterUpdateProject
    after update on employeeprojects
    for each row 
		begin
			
            declare full_name varchar(150);
            select concat(e.firstname, ' ', e.lastname) into full_name from employees e where employeeid = old.employeeid;
            
			if old.projectid <> new.projectid then
				insert into project_changes (e_id, e_fullname, old_project, new_project, date_time) values
                    (old.employeeid, full_name, old.projectid, new.projectid, now());
			end if;
        end !!
delimiter ;

delimiter !!
create procedure updateProject(in e_id int, in new_project_id int)
begin
	update employeeprojects set projectid = new_project_id where employeeid = e_id;
    select * from employeeprojects where employeeid = e_id;
end !!
delimiter ;

call updateProject(50, 4);

select * from project_changes;
select * from employeeprojects where employeeid = 50;






















