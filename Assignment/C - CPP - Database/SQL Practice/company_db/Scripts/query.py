
import random
from datetime import datetime, timedelta
from itertools import product

first_names = [
    'Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'John', 
    'Karen', 'Leo', 'Mona', 'Nina', 'Omar', 'Paul', 'Quinn', 'Rita', 'Sam', 'Tina',
    'Naruto', 'Luffy', 'Goku', 'Sakura', 'Tony', 'Bruce', 'Clark', 'Diana', 'Walter', 'Jesse',
    'Eleven', 'Jon', 'Daenerys', 'Tyrion', 'Rick', 'Morty', 'Arya', 'Frodo', 'Bilbo', 'Sherlock',
    'Jonas', 'Mikasa', 'Levi', 'Eren', 'Kenshin', 'Spike', 'Vash', 'Light', 'L', 'Natsu',
    'Karma', 'Rei', 'Asuka', 'Gintoki', 'Yusuke', 'Inuyasha', 'Ichigo', 'Rukia', 'Shinji', 'Kaname',
    'Barry', 'Oliver', 'Selina', 'Harley', 'Joker', 'Deadpool', 'Wade', 'Peter', 'Miles', 'Logan',
    'Clarkson', 'Max', 'Zara', 'Felix', 'Helena', 'Jade', 'Kai', 'Lara', 'Mia', 'Nico',
    'Oscar', 'Piper', 'Quincy', 'Ruby', 'Seth', 'Tara', 'Uma', 'Vince', 'Willow', 'Xander',
    'Yara', 'Zane', 'Alex', 'Brooke', 'Cody', 'Delia', 'Ethan', 'Fiona', 'Gavin', 'Hazel',
    'Iris', 'Jack', 'Kira', 'Liam', 'Maya', 'Nolan', 'Olive', 'Peyton', 'Quinn', 'Rhea',
    'Sage', 'Theo', 'Uma', 'Vera', 'Wade', 'Xena', 'Yosef', 'Zelda', 'Amber', 'Blake',
    'Carmen', 'Dylan', 'Elle', 'Finn', 'Gia', 'Holden', 'Isla', 'Jaxon', 'Kelsey', 'Logan',
    'Maddox', 'Nova', 'Orion', 'Paige', 'Quinn', 'Reese', 'Sawyer', 'Tessa', 'Uriah', 'Violet',
    'Wyatt', 'Ximena', 'Yanni', 'Zion', 'Anya', 'Brady', 'Cleo', 'Derek', 'Elena', 'Felipe',
    'Greta', 'Hugo', 'Imani', 'Jesse', 'Keira', 'Luca', 'Mila', 'Nash', 'Opal', 'Phoenix',
    'Quentin', 'Ryder', 'Serena', 'Trent', 'Una', 'Valen', 'Wren', 'Xavi', 'Yvette', 'Zane',
    'Aria', 'Beau', 'Chloe', 'Dante', 'Emery', 'Flynn', 'Gemma', 'Harper', 'Isaias', 'Juno'
]

last_names = [
    'Johnson', 'Smith', 'Davis', 'Brown', 'Wilson', 'Miller', 'Taylor', 'Anderson', 'Thomas', 'Moore',
    'Clark', 'Wright', 'Scott', 'Young', 'King', 'Green', 'Hall', 'Lee', 'Walker', 'Hill',
    'Stark', 'Wayne', 'Kent', 'Prince', 'White', 'Black', 'Gray', 'Gold', 'Silver', 'Bronze',
    'Simpson', 'Griffin', 'Parker', 'Stark', 'Banner', 'Strange', 'Romanoff', 'Rogers', 'Maxwell', 'Blake',
    'Ackerman', 'Yeager', 'Kurosaki', 'Uchiha', 'Hatake', 'Kamiya', 'Makunouchi', 'Mugen', 'Hellsing', 'Kiryuuin',
    'Hancock', 'Queen', 'Fox', 'Lannister', 'Targaryen', 'Snow', 'Stark', 'Bolton', 'Baratheon', 'Tyrell',
    'Fujimoto', 'Takahashi', 'Abarai', 'Kamado', 'Uzumaki', 'Shimura', 'Izumi', 'Sakata', 'Fujibayashi', 'Kusanagi',
    'Bennett', 'Chapman', 'Daniels', 'Ellis', 'Fletcher', 'Garcia', 'Harrison', 'Iverson', 'Jennings', 'Knight',
    'Larsen', 'Morrison', 'Norris', 'Owens', 'Peters', 'Quinn', 'Reynolds', 'Sullivan', 'Turner', 'Underwood',
    'Valdez', 'Wagner', 'Xavier', 'Youngblood', 'Zimmerman', 'Armstrong', 'Bradley', 'Cameron', 'Dawson', 'Evans',
    'Franklin', 'Gibson', 'Hale', 'Ingram', 'Jameson', 'Keller', 'Lawson', 'Mitchell', 'Nelson', 'Ortiz',
    'Powell', 'Quintero', 'Russell', 'Sanders', 'Taylor', 'Urban', 'Vargas', 'Watson', 'Xu', 'Yang',
    'Zimmer', 'Abbott', 'Baxter', 'Caldwell', 'Donovan', 'Ellington', 'Frost', 'Graves', 'Hayes', 'Irwin',
    'Jenkins', 'Kirk', 'Lane', 'Miles', 'Norman', 'Olsen', 'Perry', 'Quade', 'Rice', 'Sampson',
    'Thompson', 'Upton', 'Vance', 'West', 'Xander', 'York', 'Zane', 'Addison', 'Blair', 'Coleman',
    'Dean', 'Elliott', 'Fisher', 'Gordon', 'Harper', 'Innes', 'Jones', 'Kingston', 'Lewis', 'Mason',
    'Nash', 'Owens', 'Price', 'Quincy', 'Reed', 'Stewart', 'Turner', 'Vaughn', 'Walker', 'Young',
    'Zimmerman', 'Alvarez', 'Bishop', 'Cross', 'Douglas', 'Erickson', 'Fleming', 'Garrett', 'Hunt', 'Irving',
    'Jackson', 'Knight', 'Long', 'Marshall', 'Nelson', 'Oliver', 'Phillips', 'Quinn', 'Russell', 'Shaw'
]


departments = [1,2,3,4,5,6,7]
start_date = datetime(2018, 1, 1)

# Generate all possible unique name combos
unique_names = list(product(first_names, last_names))
random.shuffle(unique_names)

# File to write SQL inserts
with open("employees_insert.sql", "w", encoding="utf-8") as file:
    file.write("INSERT INTO Employees (FirstName, LastName, DepartmentID, HireDate, Salary) VALUES\n")

    for i in range(10000):
        fn, ln = unique_names[i]
        dept = random.choice(departments)
        hire_date = start_date + timedelta(days=random.randint(0, 2000))
        salary = round(random.uniform(50000, 90000), 2)
        comma = "," if i < 9999 else ";"
        line = f"('{fn}', '{ln}', {dept}, '{hire_date.strftime('%Y-%m-%d')}', {salary}){comma}\n"
        file.write(line)

print("✅ SQL insert statements saved to 'employees_insert.sql'")

