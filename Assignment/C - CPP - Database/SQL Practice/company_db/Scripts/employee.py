import mysql.connector
from faker import Faker
import random
from datetime import date


# Initialize Faker and MySQL connection
fake = Faker('en_IN')
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="company_db"
)
cursor = db.cursor()

# Anime character names list (First and Last Names)
first_names = [
    "Naruto", "Sasuke", "Sakura", "Kakashi", "Itachi", "Luffy", "Zoro", "Nami", "Sanji", "Robin",
    "Ichigo", "Rukia", "Light", "Levi", "Eren", "Mikasa", "Goku", "Vegeta", "Saitama", "Edward",
    "Killua", "Gon", "Shoto", "Izuku", "Tanjiro", "Nezuko", "Zenitsu", "Inosuke", "Giyu", "Kyojuro",
    "Shinobu", "Asuna", "Kirito", "Hinata", "Kaguya", "Todoroki", "Bakugo", "Lelouch", "Suzaku",
    "Yato", "Hiyori", "Rin", "Yukio", "Asta", "Yuno", "Inuyasha", "Kagome", "Kyo", "Tohru",
    "Ken", "Touka", "Shoyo", "Kageyama", "Alucard", "Seras", "Gintoki", "Kagura", "Yugi", "Kaiba",
    "Ryuk", "Rem", "Ram", "Emilia", "Subaru", "Shinichi", "Ran", "Kaito", "Kenshin", "Misao",
    "Kaoru", "Himura", "Saito", "Sanosuke", "Katsura", "Enishi", "Seijuro", "Shishio",
    "Walter", "Jesse", "Saul", "Skyler", "Hank", "Gus", "Mike", "Tuco", "Jane", "Holly",
    "Jon", "Daenerys", "Tyrion", "Cersei", "Arya", "Sansa", "Bran", "Ned", "Robb", "Jaime",
    "Eleven", "Mike", "Dustin", "Lucas", "Will", "Max", "Steve", "Nancy", "Jonathan",
    "Joe", "Love", "Beck", "Forty", "Marienne", "Theo", "Ellie", "Delilah", "Candace",
    "Dexter", "Debra", "Angel", "Rita", "Harrison", "Hannah", "Lumen", "Lila", "Doakes",
    "Sherlock", "John", "Mycroft", "Moriarty", "Lestrade", "Irene", "Mary",
    "Thomas", "Arthur", "Polly", "Ada", "John", "Michael", "Finn", "Alfie",
    "Berlin", "Tokyo", "Nairobi", "Denver", "Rio", "Helsinki", "Oslo", "Lisbon",
    "Lagertha", "Bjorn", "Ragnar", "Floki", "Ivar", "Ubbe", "Hvitserk", "Rollo",
    "Akira", "Yusuke", "Mitsuki", "Hinori", "Riko", "Chihiro", "Shinji", "Misaki", "Yuuto", "Ayumi",
    "Kaito", "Mika", "Yuki", "Tsubasa", "Nanami", "Yuichi", "Ryo", "Kazuto", "Nao", "Makoto",
    "Aoi", "Rei", "Sora", "Haruto", "Tomo", "Ren", "Takumi", "Riku", "Haru", "Miku", "Arata",
    "Kohaku", "Shiro", "Takeshi", "Kaoru", "Ryoma", "Takashi", "Tatsuya", "Miyu", "Kei", "Fujin",
    "Reiji", "Saori", "Yuina", "Shiori", "Tetsuya", "Daiki", "Hikaru", "Koutarou", "Hiroshi",
    "Shun", "Haruki", "Shizuka", "Tomoya", "Kazuki", "Kyohei", "Seiji", "Masa", "Eiji"
]

last_names = [
    "Uzumaki", "Uchiha", "Haruno", "Hatake", "Hyuga", "Monkey D.", "Roronoa", "Vinsmoke", "Nico",
    "Kurosaki", "Kuchiki", "Yagami", "Ackerman", "Yeager", "Son", "Zoldyck", "Freecss", "Todoroki",
    "Midoriya", "Kamado", "Agatsuma", "Hashibira", "Tomioka", "Rengoku", "Kocho", "Abarai",
    "Hoshigaki", "Sarutobi", "Yamamoto", "Tsunayoshi", "Sawada", "Hibari", "Kiryuuin", "Kamui",
    "Shiba", "Shihouin", "Kyoraku", "Urahara", "Kuchiki", "Ishida", "Hoshigaki", "Matsumoto",
    "White", "Pinkman", "Goodman", "Schrader", "Fring", "Ehrmantraut", "Salamanca", "Margolis", "White",
    "Snow", "Targaryen", "Lannister", "Stark", "Baratheon", "Greyjoy", "Mormont", "Tyrell", "Sand",
    "Hopper", "Byers", "Sinclair", "Harrington", "Wheeler", "Mayfield", "Munson", "Driscoll",
    "Goldberg", "Quinn", "Salinger", "Geller", "Kepner", "Morgan", "Bateman", "Bridgers", "Spencer",
    "Morgan", "Lopez", "Ramirez", "Bennet", "Dawson", "Flynn", "Murphy", "Grant",
    "Holmes", "Watson", "Adler", "Moran", "Gregson", "Hudson", "Shelby", "Gray", "Thorne", "Campbell", "Changretta",
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "Sakamoto", "Aomine", "Takamura", 
    "Fujimoto", "Miyazaki", "Kisaragi", "Sakurai", "Shiba", "Yamato", 
    "Takeda", "Ishikawa", "Ohtsuki", "Fujita", "Umeda", "Sudo", "Hoshino", "Saeki", "Nakamura",
    "Kuroda", "Mikami", "Iida", "Rikimaru", "Kurosawa", "Goto", "Tajima", "Seki", "Kanemoto", "Nakamura",
    "Katori", "Kageyama", "Higa", "Tsuda", "Sato", "Takeuchi", "Ono", "Shimizu", "Aoki", "Kobayashi",
    "Nanase", "Koyama", "Kondo", "Shiratori", "Utsunomiya", "Kaneko", "Nishida", "Taguchi", "Kureha", 
    "Seki", "Takamatsu", "Sawada", "Fujii", "Kageura", "Kobayakawa", "Hirata", "Nagai"
]




departments = [
    "Human Resources", "Information Technology", "Finance", "Marketing", "Sales",
    "Operations", "Customer Service", "Logistics", "Procurement", "Legal",
    "R&D", "Engineering", "Product Management", "Design", "Quality Assurance",
    "Business Development", "Public Relations", "Administration", "Training", "Facilities",
    "Strategy", "Risk Management", "Compliance", "Internal Audit", "Digital Transformation",
    "Cybersecurity", "Data Science", "AI Lab", "DevOps", "Technical Writing",
    "UX Research", "Cloud Infrastructure", "Mobile Development", "Game Development", "AR/VR Division"
]
for dept in departments:
    cursor.execute("INSERT INTO departments (dept_name) VALUES (%s)", (dept,))
db.commit()

projects = [
    "Project Apollo", "Project Titan", "Project Orion", "Project Phoenix", "Project Horizon",
    "Project Neptune", "Project Aurora", "Project Gemini", "Project Eclipse", "Project Helios",
    "Project Mercury", "Project Atlas", "Project Vega", "Project Nova", "Project Comet",
    "Project Quantum", "Project Zenith", "Project Terra", "Project Solaris", "Project Cyclone",
    "Project Vanguard", "Project Summit", "Project Omega", "Project Genesis", "Project Odyssey",
    "Project Infinity", "Project Polaris", "Project Luna", "Project Vortex", "Project Mirage",
    "Project Sierra", "Project Equinox", "Project Vertex", "Project Cascade", "Project Ember",
    "Project Prism", "Project Keystone", "Project Horizon-X", "Project Stellar", "Project Nimbus",
    "Project Arcadia", "Project Drift", "Project Zenith-X", "Project Fusion", "Project Ignite",
    "Project Spectra", "Project Pulse", "Project Element", "Project Summit-X", "Project Vertex-X",
    "Project Aether", "Project Velocity", "Project Zenith Prime", "Project Echo", "Project Origin",
    "Project Apex", "Project Nexus", "Project Legacy", "Project Realm", "Project Axis", "Project Strive",
    "Project Eclipse-X", "Project Radiant", "Project Solstice", "Project Phoenix-X", "Project Titan-X",
    "Project Halo", "Project Equator", "Project Nova-X", "Project Infinity-X", "Project Catalyst",
    "Project Obsidian", "Project Borealis", "Project Zephyr", "Project Typhoon", "Project Altair",
    "Project Nebula", "Project Monolith", "Project Radiance", "Project Chronos", "Project Synth"
]

for proj in projects:
    dept_id = random.randint(1, len(departments))
    cursor.execute("INSERT INTO projects (project_name, dept_id) VALUES (%s, %s)", (proj, dept_id))
db.commit()

num_employees = 137540
positions = ['Manager', 'Developer', 'Analyst', 'HR', 'Sales', 'Consultant', 'Technician']
genders = ['Male', 'Female', 'Other']

# Department and project weights
dept_weights = sorted([random.randint(1, 15) for _ in range(len(departments))], reverse=True)
project_weights = sorted([random.randint(1, 10) for _ in range(len(projects))], reverse=True)

# Fetch current project count
cursor.execute("SELECT COUNT(*) FROM projects")
num_projects = cursor.fetchone()[0]

# # Dynamic project weights
# high_weight = 10
# medium_weight = 5
# low_weight = 1
# if num_projects <= 10:
#     project_weights = [high_weight] * num_projects
# elif num_projects <= 30:
#     project_weights = [high_weight] * 10 + [medium_weight] * (num_projects - 10)
# else:
#     remaining = num_projects - 30
#     project_weights = [high_weight] * 10 + [medium_weight] * 20 + [low_weight] * remaining

for i in range(num_employees):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower().replace(' ', '')}@anime.com"
    phone = fake.phone_number()
    position = random.choice(positions)
    
    gender = random.choices(
        population=['Male', 'Female', 'Other'],
        weights=[60, 37.66, 2.34],  # Total = 100%
        k=1
    )[0]

    dob = fake.date_of_birth(minimum_age=20, maximum_age=60)
    dept_id = random.choices(range(1, len(departments)+1), weights=dept_weights, k=1)[0]
    project_id = random.choices(range(1, num_projects+1), weights=project_weights, k=1)[0]
    
    # Weighted date ranges: more recent years have more hires
    year_weights = [
        (2024, 20), (2023, 20), (2022, 15),
        (2021, 10), (2020, 5),  # Pandemic slump
        (2019, 10), (2018, 10), (2017, 5), (2016, 3), (2015, 2)
    ]

    years, weights = zip(*year_weights)
    selected_year = random.randint(2010, 2024)
    start_date = date(selected_year, 1, 1)
    end_date = date(selected_year, 12, 31)
    hire_date = fake.date_between(start_date=start_date, end_date=end_date)


    # Salary fluctuates more by department group
    base = random.randint(30, 150) * 1000
    dept_salary_modifier = random.uniform(0.8, 1.2) * dept_weights[dept_id - 1] / max(dept_weights)
    salary = round(base * dept_salary_modifier, 2)
    
    cursor.execute("""
        INSERT INTO employees (first_name, last_name, email, phone_number, position, gender, date_of_birth, dept_id, project_id, hire_date, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, email, phone, position, gender, dob, dept_id, project_id, hire_date, salary))

    if (i+1) % 5000 == 0:
        db.commit()
        print(f"{i+1} records inserted...")

db.commit()
print("✅ All 100,000 records inserted successfully!")

cursor.close()
db.close()
