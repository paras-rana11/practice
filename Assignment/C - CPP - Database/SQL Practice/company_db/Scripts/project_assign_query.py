import random

start_employee_id = 51
end_employee_id = 9000
project_ids = list(range(1, 51))  # Projects 1 to 50

with open("EmployeeProjects_insert.sql", "w", encoding="utf-8") as file:
    file.write("INSERT INTO EmployeeProjects (EmployeeID, ProjectID) VALUES\n")

    for emp_id in range(start_employee_id, end_employee_id + 1):
        proj_id = random.choice(project_ids)
        comma = "," if emp_id < end_employee_id else ";"
        line = f"({emp_id}, {proj_id}){comma}\n"
        file.write(line)

print("File 'EmployeeProjects_insert.sql' created successfully!")
