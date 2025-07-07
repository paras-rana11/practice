import mysql.connector

def print_results(label, data, column_names=None):
    print(label)
    print("-----------------------------------------")
    if column_names:
        print("Column Names: ", column_names)
    for row in data:
        print(row)
    print("\n")
    
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="practice"  # Connecting to the 'practice' database
)

query = conn.cursor()

q = "SHOW DATABASES"
query.execute(q)

databases = query.fetchall()

print("Databases in the MySQL server:")
print("-----------------------------")
print("fetchall type: ", type(databases))
print("Databases List: ", databases, "\n")


# Execute the query to switch to the 'Test' database. After query.execute("USE Test"), you don't need to call fetchone() because the USE command doesn't return any result.
q1 = "USE Test"
query.execute(q1)

q2 = "SELECT DATABASE()"
query.execute(q2)
current_db = query.fetchone()

print("Current Database after switching to 'Test':")
print("-----------------------------------------")
print("fetchone type: ", type(current_db))
print("Current Database: ", current_db[0], "\n")  # current_db is a tuple, so we access the first element

# Switching back to 'practice' database
q3 = "USE practice"
query.execute(q3)

q4 = "SELECT DATABASE()"
query.execute(q4)
current_db = query.fetchone()

print("Current Database after switching to 'Practice':")
print("-----------------------------------------")
print("fetchone type: ", type(current_db))
print("Current Database: ", current_db[0], "\n")  # current_db is a tuple, so we access the first element


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

q5 = "SHOW TABLES"
query.execute(q5)
tables = query.fetchall()
print_results("Tables in Current Database 'Practice':", tables)


# # Listing procedures, functions, and triggers

# # To list stored procedures
# q6 = "SHOW PROCEDURE STATUS WHERE Db = 'practice'"
# query.execute(q6)
# procedures = query.fetchall()
# print_results("Stored Procedures in 'Practice' Database:", procedures)

# # To list functions
# q7 = "SHOW FUNCTION STATUS WHERE Db = 'practice'"
# query.execute(q7)
# functions = query.fetchall()
# print("Functions in 'Practice' Database:", functions)

# # To list triggers
# q8 = "SHOW TRIGGERS WHERE `Database` = 'practice'"
# query.execute(q8)
# triggers = query.fetchall()
# print("Triggers in 'Practice' Database:", triggers)

# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

q9 = "SELECT * FROM Employees"
query.execute(q9)
employees = query.fetchall()

# print(query.description)
column_names = [i[0] for i in query.description]  # Get column names from cursor's description

print_results("Employees: ", employees[:5], column_names)
 
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
    
q10 = "select * from employees where salary > 100000"
q10_1 = "select * from employees where firstname like 'A%'"
q10_2 = "select avg(salary) from employees"
q10_3 = "select DepartmentID, count(EmployeeID) as emp_in_dept, sum(salary) as total_salary_in_dept from employees group by DepartmentID "
q10_4 = "select DepartmentID, count(EmployeeID) as emp_in_dept, sum(salary) as total_salary_in_dept from employees group by DepartmentID having emp_in_dept > 6"


query.execute(q10_3)
filtered_emps = query.fetchall()

column_names = [i[0] for i in query.description]  # Get column names from cursor's description

print_results("Filtered Employees:", filtered_emps, column_names)


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

q11 = ''' 
        INSERT INTO Employees (FirstName, LastName, DepartmentID, HireDate, Salary) 
        VALUES
            ('Naruto', 'Uzumaki', 2, '2023-04-01', 500000.00),
            ('Sasuke', 'Uchiha', 3, '2023-05-12', 150000.00),
            ('Kakashi', 'Hatake', 2, '2023-04-01', 100000.00),
            ('Madara', 'Uchiha', 3, '2023-05-12', 200000.00);
      '''
      
# query.execute(q11)
conn.commit()

print_results("Employees: ", employees[50:], column_names)


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


q12 = "INSERT INTO Employees (FirstName, LastName, DepartmentID, HireDate, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [ ('Michael', 'Scofield', 1, '2023-04-01', 500000.00),
        ('Linc', 'Burrows', 3, '2023-05-12', 150000.00),
        ('Gretchen', 'Morgan', 5, '2023-04-01', 100000.00),
        ('Christina', 'Rose', 3, '2023-05-12', 200000.00)
      ]

# query.executemany(q12, val)

conn.commit()


print_results("Employees: ", employees[50:], column_names)


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦







# Closing the cursor and connection
query.close()
conn.close()

# Success message with newline
print("\nSuccess\n")
