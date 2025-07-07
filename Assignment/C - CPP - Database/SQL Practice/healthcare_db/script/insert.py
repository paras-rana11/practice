
import mysql.connector
from faker import Faker
import random
from tqdm import tqdm

# Initialize Faker
fake = Faker()
Faker.seed(42)
random.seed(42)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root1',
    'database': 'healthcare',
    'connection_timeout': 600
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Sample data for names
web_series_names = [
    'Walter White', 'Jesse Pinkman', 'Saul Goodman', 'Skyler White', 'Tony Soprano', 'Don Draper', 'Dexter Morgan', 'Rick Grimes', 'Daryl Dixon', 'Michonne', 'Jon Snow', 'Daenerys Targaryen', 
    'Tyrion Lannister', 'Cersei Lannister', 'Arya Stark', 'Sansa Stark', 'Tommy Shelby', 'Peaky Blinders', 'Elena Gilbert', 'Stefan Salvatore',  'Damon Salvatore', 'Rick Castle', 'Kate Beckett', 'Sherlock Holmes','John Watson', 'BoJack Horseman', 'Betty Draper', 'Don Draper', 'Frank Underwood', 'Claire Underwood', 'Hannah Baker', 'Clay Jensen', 'Jonah Hill', 'Lena Dunham', 'Elliot Alderson', 'Angela Moss', 'Rachel Green', 'Monica Geller', 'Chandler Bing', 'Phoebe Buffay',  'Ross Geller', 'Joey Tribbiani', 'Michael Scott', 'Jim Halpert', 
    'Pam Beesly', 'Dwight Schrute', 'Angela Martin', 'Stanley Hudson', 'Ryan Howard', 'Oscar Martinez', 'Kelly Kapoor', 'Creed Bratton', 'Ryan Atwood', 'Seth Cohen', 'Marissa Cooper', 'Summer Roberts',  'Sandy Cohen', 'Kirsten Cohen', 'Dylan McKay', 'Brenda Walsh',  'Luke Perry', 'Blair Waldorf', 'Serena van der Woodsen', 'Chuck Bass', 'Dan Humphrey', 'Jenny Humphrey', 'Nate Archibald', 'Georgina Sparks', 'Vanya Hargreeves', 'Luther Hargreeves', 'Diego Hargreeves',   'Klaus Hargreeves', 'Allison Hargreeves', 'Five Hargreeves', 'Ben Hargreeves', 'Reginald Hargreeves', 'Hazel', 'Cha-Cha', 'The Governor', 'Negan',  'Carol Peletier', 'Glenn Rhee', 'Maggie Greene', 'Rick Grimes', 'Merle Dixon', 'Eugene Porter', 'Abraham Ford', 'Rosita Espinosa', 'Shane Walsh', 'Andrea Harrison', 'Theon Greyjoy', 'Joffrey Baratheon', 'Samwell Tarly', 'Varys', 'Jaime Lannister', 'Brienne of Tarth', 'Petyr Baelish',  'Melisandre', 'Sansa Stark', 'Arya Stark', 'Robb Stark', 'Catelyn Stark', 'Ned Stark', 'Hodor', 'Jorah Mormont', 'Tyrion Lannister', 'Cersei Lannister',  'Jamie Lannister', 'Brienne of Tarth', 'Missandei', 'Grey Worm', 'Oberyn Martell', 'Tywin Lannister', 'Bronn', 'Varys', 'Ramsay Bolton', 'Ramsay Snow', 'Hound', 'The Mountain', 'Podrick Payne', 'Tormund Giantsbane', 'Ygritte', 'Jon Snow', 'Theon Greyjoy', 'Benjen Stark', 'Renly Baratheon', 'Margaery Tyrell', 'Loras Tyrell', 'Selyse Baratheon', 'Shireen Baratheon', 'Myrcella Baratheon', 'Tommen Baratheon', 'Tyrion Lannister', 'Lancel Lannister',  'Melisandre', 'Stannis Baratheon', 'Davos Seaworth', 'Asha Greyjoy', 'Euron Greyjoy', 'Samwell Tarly', 'Bran Stark', 'Jorah Mormont', 'Missandei', 'Jaqen H’ghar', 'Tormund Giantsbane', 'Nikolaj Coster-Waldau', 'Kit Harington'
]


anime_names = [
    'Naruto Uzumaki', 'Sasuke Uchiha', 'Sakura Haruno', 'Kakashi Hatake', 'Goku', 'Vegeta', 'Gohan', 'Piccolo', 'Luffy', 'Zoro', 'Nami', 'Sanji', 'Ichigo Kurosaki', 'Rukia Kuchiki', 'Light Yagami', 'L Lawliet', 'Edward Elric', 'Alphonse Elric', 'Roy Mustang', 'Riza Hawkeye', 'Winry Rockbell', 'Faye Valentine', 'Spike Spiegel', 'Jet Black', 'Vicious', 'Ein', 'Kagome Higurashi', 'Inuyasha', 'Sesshomaru', 'Miroku', 'Sango', 'Shippou', 'Kikyo', 'Naraku', 'Natsu Dragneel', 'Lucy Heartfilia', 'Erza Scarlet', 'Gray Fullbuster', 'Wendy Marvell', 'Juvia Lockser', 'Levy McGarden', 'Mirajane Strauss', 'Laxus Dreyar', 'Tatsumi', 'Mine', 'Akame', 'Esdeath', 'Lubbock', 'Seryu Ubiquitous', 'Dr. Stylish', 'Maka Albarn', 'Soul Eater', 'Black☆Star', 'Tsubaki Nakatsukasa', 'Death the Kid', 'Liz Thompson', 'Patty Thompson', 'Shinigami-sama', 'Rintarou Okabe', 'Kurisu Makise', 'Mayuri Shiina', 'Suzuha Amane', 'Kyouma Hyouin', 'Yukino Yukinoshita', 'Hachiman Hikigaya', 'Yui Yuigahama', 'Chika Fujiwara', 'Emilia', 'Rem', 'Ram', 'Ainz Ooal Gown', 'Albedo', 'Shalltear Bloodfallen', 'Demiurge', 'Cocytus', 'Narberal Gamma', 'Shizu', 'Chocolat', 'Kamina', 'Simon', 'Yoko Littner', 'Nia Teppelin', 'Viral', 'Lord Genome', 'Lelouch vi Britannia', 'Suzaku Kururugi', 'C.C.', 'Kallen Stadtfeld', 'Rolo Lamperouge', 'Shirley Fenette', 'Kaguya Shinomiya', 'Miyuki Shirogane', 'Chika Fujiwara', 'Hayasaka Ai', 'Miko Iino', 'Yotsuba Nakano', 'Itsuki Nakano', 'Nino Nakano', 'Ichika Nakano', 'Fuutarou Uesugi', 'Haru Ichida', 'Ken Kaneki', 'Touka Kirishima', 'Rize Kamishiro', 'Hideyoshi Nagachika', 'Shuu Tsukiyama', 'Ayato Kirishima', 
    'Mikasa Ackerman', 'Eren Yeager', 'Armin Arlert', 'Levi Ackerman', 'Erwin Smith', 'Jean Kirstein', 'Sasha Blouse', 'Connie Springer', 'Historia Reiss', 'Reiner Braun', 'Bertolt Hoover', 'Annie Leonhart', 'Zeke Yeager', 'Ymir Fritz', 'Nina Tucker', 'Hange Zoë', 'Marco Bott', 'Flocke Forster', 'Porco Galliard', 'Pieck Finger', 'Eren Kruger', 'Rosa', 'Rochelle', 'Saitama', 'Genos', 'Mumen Rider', 'Speed-o-Sound Sonic', 'Kageyama Tobio', 'Hinata Shoyo', 'Yu Nishinoya', 'Daichi Sawamura', 'Asahi Azumane', 'Tobio Kageyama', 'Shoyo Hinata', 'Kenma Kozume', 'Yu Takeda', 'Suga Kiyoko', 'Tetsurou Kuroo', 'Tadashi Yamaguchi', 'Ittetsu Takeda', 'Ryouta Kise', 'Shintaro Midorima', 'Daiki Aomine', 'Tatsuya Himuro', 'Seijuuro Shin', 'Satsuki Momoi', 'Kuroko Tetsuya', 'Kagami Taiga', 'Midorima Shintaro', 'Akashi Seijuro', 'Imayoshi Shoichi', 'Kiyoshi Teppei', 'Murasakibara Atsushi', 'Sakurai Ryo', 'Mibuchi Reo', 'Midorima', 'Nagisa Shiota'
]

disease_names_list = [
    'Acne', 'Addison\'s Disease', 'Adenovirus', 'Aflatoxicosis', 'Alport Syndrome', 'Alzheimer\'s Disease', 'Anemia', 'Angina Pectoris', 'Anthrax', 'Aortic Aneurysm', 'Arrhythmia', 'Asthma', 'Athlete\'s Foot', 'Autism Spectrum Disorder', 'Autoimmune Disease', 'Babesiosis', 'Bacterial Meningitis', 'Benign Prostatic Hyperplasia','Bipolar Disorder', 'Bladder Cancer', 'Blood Clots', 'Bone Cancer', 'Bowel Cancer', 'Bronchitis', 'Bulimia Nervosa', 'Celiac Disease', 'Cerebral Palsy', 'Chickenpox', 'Cholera', 'Chronic Fatigue Syndrome', 'Chronic Obstructive Pulmonary Disease (COPD)', 'Cirrhosis', 'Cleft Palate', 'Cluster Headaches', 'Colitis', 'Colon Cancer', 'Common Cold', 'Conjunctivitis', 'Coronary Artery Disease',
    'Cystic Fibrosis', 'Dengue Fever', 'Depression', 'Dermatitis', 'Diabetes Mellitus', 'Diabetic Neuropathy', 'Dialysis',  'Diphtheria', 'Down Syndrome', 'Dyslexia', 'Ebola Virus', 'Emphysema', 'Endometriosis', 'Epilepsy', 'Erectile Dysfunction', 'Esophageal Cancer', 'Fibromyalgia', 'Food Poisoning', 'Fractures', 'Gastroenteritis', 'Gastric Cancer', 'Gastroesophageal Reflux Disease', 'Glaucoma', 'Gout', 'Hansen\'s Disease', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Herniated Disc', 'Herpes Simplex Virus', 'Hodgkin\'s Lymphoma', 'Human Immunodeficiency Virus (HIV)', 'Hyperthyroidism', 'Hypertension', 'Hypoglycemia', 'Hypothyroidism', 'Irritable Bowel Syndrome',  'Kidney Disease', 'Knee Osteoarthritis', 'Leukemia', 'Liver Cancer', 'Liver Disease', 'Lupus', 'Malaria', 'Measles', 'Meningitis',   'Mental Retardation', 'Migraine', 'Multiple Sclerosis', 'Myocardial Infarction', 'Myopia', 'Narcolepsy', 'Nephritis', 'Neuropathy',   'Osteoarthritis', 'Osteoporosis', 'Parkinson\'s Disease', 'Peptic Ulcer Disease', 'Pneumonia', 'Poliomyelitis', 'Prostate Cancer',   'Psoriasis', 'Pulmonary Embolism', 'Rheumatoid Arthritis', 'Rosacea', 'Salmonella Infection', 'Schizophrenia', 'Sickle Cell Anemia',   'Sinusitis', 'Skin Cancer', 'Sleep Apnea', 'Stroke', 'Syphilis', 'Tachycardia', 'Tuberculosis', 'Ulcerative Colitis', 'Urinary Tract Infection', 'Uterine Cancer', 'Varicella', 'Viral Hepatitis', 'Vitiligo', 'Whooping Cough', 'Zika Virus', 'Acromegaly', 'Aortic Dissection', 'Astigmatism',  'Atypical Pneumonia', 'Bipolar Disorder Type 2', 'Brachial Plexus Injury', 'Chagas Disease', 'Chronic Kidney Disease', 'Chronic Sinusitis',  'Chronic Urticaria', 'Clostridium Difficile Infection', 'Cognitive Impairment', 'Congenital Heart Disease', 'Craniofacial Anomalies', 'Cystitis', 'Cytomegalovirus',  'Dandy-Walker Syndrome', 'Deafness', 'Delirium', 'Dementia', 'Diabetic Retinopathy', 'Ehlers-Danlos Syndrome', 'Encephalitis', 'Endocarditis', 'Epiglottitis',  'Fibrocystic Breast Disease', 'Frontal Lobe Damage', 'Giant Cell Arteritis', 'Glomerulonephritis', 'Gonorrhea', 'Heart Failure', 'Hemophilia', 'Herpes Zoster',  'Hirschsprung Disease', 'Hydrocephalus', 'Hypereosinophilic Syndrome', 'Hyperlipidemia', 'Hyperparathyroidism', 'Hypokalemia', 'Hypoparathyroidism',  'Hypercalcemia', 'Hyperhidrosis', 'Hyperlipidemia', 'Hyperpigmentation', 'Hypertrophic Cardiomyopathy', 'Hypotension', 'Icterus', 'Infective Endocarditis', 'Interstitial Lung Disease', 'Irritable Bowel Syndrome', 'Legionnaires\' Disease', 'Leprosy', 'Lupus Erythematosus', 'Lymphoma', 'Lyme Disease',  'Mastitis', 'Menopause', 'Metabolic Syndrome', 'Meningococcal Infection', 'Mental Illness', 'Meningococcal Disease', 'Mumps', 'Myasthenia Gravis', 'Neuroblastoma', 'Neurodegenerative Disease', 'Neurofibromatosis', 'Neuropsychological Disorders', 'Non-Hodgkin\'s Lymphoma', 'Ocular Hypertension', 'Osteosarcoma', 'Ovarian Cancer', 'Pancreatic Cancer', 'Peptic Ulcer', 'Pernicious Anemia', 'Peritoneal Cancer', 'Pneumonitis', 'Polymyositis', 'Post-Traumatic Stress Disorder', 'Prostate Hyperplasia', 'Pulmonary Fibrosis', 'Raynaud\'s Disease', 'Retinal Detachment', 'Rheumatic Fever', 'Rheumatic Heart Disease', 'Sarcoidosis', 'Sepsis', 'Shingles', 'Sickle Cell Disease', 'Smallpox', 'Spina Bifida', 'Spondylitis', 'Stomach Cancer', 'Strep Throat', 'Systemic Lupus Erythematosus', 'Thyroid Cancer', 'Toxoplasmosis', 'Trigeminal Neuralgia', 'Tuberculous Meningitis', 'Typhoid Fever', 'Ulcer', 'Urinary Incontinence', 'Viral Infections', 'Viral Meningitis', 'Wernicke\'s Encephalopathy', 'Wilson\'s Disease', 'Zellweger Syndrome', 'Zoonotic Disease', 'Achilles Tendinitis', 'Adenocarcinoma', 'Adrenal Gland Disorder', 'Albinism', 'Allergies', 'Alopecia Areata', 'Aortic Valve Disease', 'Arterial Disease', 'Basal Cell Carcinoma', 'Bell\'s Palsy', 'Benign Tumors', 'Biliary Atresia', 'Bladder Infection', 'Blood Disorders', 'Bone Marrow Disorders', 'Bowel Obstruction', 'Brain Tumors', 'Bronchiectasis', 'Bulging Disc', 'Bursitis', 'Cervical Cancer', 'Cervical Spondylosis', 'Chronic Migraines', 'Cirrhosis of the Liver', 'Colon Polyps', 'Common Cold Virus', 'Congenital Anomalies', 'Corneal Ulcer', 'Cysticercosis', 'Deep Vein Thrombosis', 'Dementia with Lewy Bodies', 'Dizziness', 'Endocrine Tumors', 'Epileptic Seizures', 'Excessive Sweating', 'Eye Infections', 'Gallstones','Gastroparesis', 'Gingivitis', 'Hantavirus', 'Hemorrhoids', 'Hodgkin\'s Disease', 'Hypospadias', 'Immunodeficiency Syndrome', 'Infectious Mononucleosis', 'Influenza', 'Kawasaki Disease', 'Liver Failure', 'Lung Cancer', 'Lymphadenopathy', 'Malignant Melanoma', 'Melasma', 'Meningitis B', 'Menstrual Disorders', 'Molar Pregnancy', 'Multiple Myeloma', 'Osteogenesis Imperfecta', 'Peptic Ulcer Disease', 'Pericarditis', 'Pneumothorax', 'Polymyalgia Rheumatica', 'Post-Surgical Infection', 'Pulmonary Arterial Hypertension', 'Renal Failure', 'Rheumatoid Lung Disease', 'Sarcoma', 'Scleroderma', 'Secondary Hypertension', 'Skin Disorders', 'Spinal Cord Injury', 'Spinal Stenosis', 'Spondylolisthesis', 'Squamous Cell Carcinoma', 'Systemic Sclerosis', 'Thyroid Disorders', 'Tinnitus', 'Tonsillitis', 'Toxic Shock Syndrome','Tubular Acidosis', 'Vasculitis', 'Viral Myocarditis', 'Warts', 'Whipple\'s Disease'
]


disease_names = set(disease_names_list)

# Insert diseases
# print("Inserting diseases...")
# disease_ids = []
# for disease_name in tqdm(disease_names):
#     cursor.execute("INSERT INTO diseases (disease_name) VALUES (%s)", (disease_name,))
#     disease_ids.append(cursor.lastrowid)
# conn.commit()

# departments_list = ['Cardiology', 'Neurology', 'Oncology', 'Pediatrics', 'Orthopedics', 'Dermatology', 'Psychiatry', 'Radiology', 'Anesthesiology', 'Emergency Medicine', 'Endocrinology', 'Gastroenterology', 'Hematology', 'Nephrology', 'Ophthalmology', 'Pathology', 'Pulmonology', 'Rheumatology', 'Urology', 'General Surgery', 'Plastic Surgery', 'Infectious Disease', 'Allergy and Immunology', 'Geriatrics', 'Obstetrics and Gynecology', 'Otolaryngology', 'Pain Management', 'Palliative Care', 'Physical Medicine and Rehabilitation', 'Sleep Medicine', 'Sports Medicine', 'Transplant Surgery', 'Vascular Surgery', 'Critical Care Medicine', 'Hospital Medicine', 'Internal Medicine', 'Medical Genetics', 'Nuclear Medicine', 'Preventive Medicine', 'Reproductive Endocrinology', 'Thoracic Surgery', 'Trauma Surgery', 'Urgent Care', 'Wound Care', 'Occupational Medicine', 'Hyperbaric Medicine', 'Clinical Pharmacology', 'Medical Toxicology', 'Forensic Pathology', 'Anatomical Pathology', 'Laboratory Medicine', 'Immunology', 'Bioinformatics', 'Radiation Oncology', 'Molecular Medicine', 'Pediatric Surgery', 'Cardiothoracic Surgery', 'Geriatric Psychiatry', 'Viral Disease', 'Bariatric Surgery', 'Dental Surgery', 'Plastic and Reconstructive Surgery', 'Gastrointestinal Surgery', 'Liver Transplantation', 'Endovascular Surgery', 'Pediatric Cardiology', 'Vascular Interventional Radiology', 'Neuroendocrinology', 'Hepatology', 'Obstetric Ultrasound', 'Sports Rehabilitation', 'Pediatric Infectious Diseases', 'Dermatopathology', 'Infectious Disease Pathology', 'Pulmonary Rehabilitation', 'Child and Adolescent Psychiatry', 'Spinal Surgery', 'Neurointerventional Radiology', 'Neurophysiology', 'Biostatistics', 'Rehabilitation Psychology', 'Electrophysiology', 'Cardiac Electrophysiology', 'Breast Surgery', 'Urogynecology', 'Orthopedic Oncology', 'Endocrine Surgery', 'Pediatric Pulmonology', 'Oncologic Surgery', 'Obesity Medicine', 'Neuro-oncology', 'Sleep Surgery', 'Advanced Heart Failure', 'Gerontological Nursing', 'Elder Care', 'Phlebology', 'Addiction Medicine', 'Psychosomatic Medicine', 'Pediatric Rheumatology', 'Pediatric Nephrology', 'Functional Medicine', "Men's Health", 'Integrative Medicine', 'Geriatric Medicine', 'Pediatric Endocrinology', 'Sleep Psychology', 'Spine Surgery', 'Cardiac Surgery', 'Orthotic and Prosthetic Services', 'Vascular Neurology', 'Musculoskeletal Oncology', 'Pain Management Psychiatry', 'Veterinary Medicine', 'Trauma and Burn Surgery', 'Pediatric Hematology', 'Sexual Medicine', 'Medical Imaging', 'Behavioral Neurology', 'Foot and Ankle Surgery', 'Surgical Oncology', 'Wound and Ostomy Care', 'Cancer Genetics', 'Interventional Pain Management', 'Clinical Immunology', 'Plastic and Aesthetic Surgery', 'Endoscopic Surgery', 'Acute Care Surgery', 'Health Informatics', 'Family Medicine', 'Liver Disease', 'Perinatal Psychiatry', 'Cardiac Imaging', 'Trauma Critical Care', 'Therapeutic Endoscopy', 'Surgical Pathology', 'Vascular Medicine', 'Hepato-pancreatico-biliary Surgery', 'Orthopedic Sports Medicine', 'Adult Congenital Heart Disease', 'Clinical Genetics', 'Neurogenetics', 'Perinatal Medicine', 'Emergency Ultrasound', 'Pediatric Otolaryngology', 'Hand Surgery', 'Functional Neurosurgery', 'Pediatric Orthopedics', 'Chronic Pain Management', 'Hematologic Oncology', 'Invasive Cardiology', 'Reproductive Medicine', 'Fertility Medicine', 'Maternal Fetal Medicine', 'Emergency Cardiology']

# # Insert departments
# print("Inserting departments...")
# department_ids = []
# for dept in tqdm(departments_list):
#     cursor.execute("INSERT INTO departments (dept_name) VALUES (%s)", (dept,))
#     department_ids.append(cursor.lastrowid)
# conn.commit()

department_ids = list(range(1, 155))

# Insert doctors
print("Inserting doctors...")
doctor_ids = []
for _ in tqdm(range(1800)):
    full_name = random.choice(anime_names)
    gender = random.choices(['Male', 'Female', 'Other'], weights=[50, 45, 5])[0]
    specialization = fake.job()
    country = random.choices(['India'] + [fake.country() for _ in range(5)], weights=[20] + [6]*5)[0]
    doctor_type = 'local' if country == 'India' else 'foreign'
    license_number = fake.bothify(text='??#####')
    
    weights = []
    for dept_id in department_ids:
        if dept_id % 7 == 0:
            weights.append(8)   # moderately popular
        elif dept_id % 13 == 0:
            weights.append(12)  # more popular
        else:
            weights.append(1)   # default

    dept_id = random.choices(department_ids, weights=weights, k=1)[0]


    cursor.execute("""
        INSERT INTO doctors (full_name, gender, specialization, doctor_type, country_of_origin, license_number, dept_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (full_name, gender, specialization, doctor_type, country, license_number, dept_id))
    doctor_ids.append(cursor.lastrowid)
conn.commit()

# print("Inserting patients...")
# patient_ids = []
# batch_size = 1000
# for _ in tqdm(range(0, 247540, batch_size)):
#     for _ in range(batch_size):
#         full_name = random.choice(anime_names)
#         gender = random.choices(['Male', 'Female', 'Other'], weights=[57, 40, 3])[0]
        
#         age_group = random.choices(
#             population=["child", "adult", "elderly"],
#             weights=[1, 5, 3],  # more adults, then elderly
#             k=1
#         )[0]

#         if age_group == "child":
#             dob = fake.date_of_birth(minimum_age=0, maximum_age=14)
#         elif age_group == "adult":
#             dob = fake.date_of_birth(minimum_age=15, maximum_age=59)
#         else:
#             dob = fake.date_of_birth(minimum_age=60, maximum_age=90)
            
#         country = random.choices(['India'] + [fake.country() for _ in range(5)], weights=[70] + [6]*5)[0]
#         patient_type = 'local' if country == 'India' else 'foreign'

#         cursor.execute("""
#             INSERT INTO patients (full_name, gender, date_of_birth, patient_type, country_of_origin)
#             VALUES (%s, %s, %s, %s, %s)
#         """, (full_name, gender, dob, patient_type, country))
#         patient_ids.append(cursor.lastrowid)
#     conn.commit()
    
    
# patient_ids = [ i for i in range(1, 481000) ]  
    
# Insert patient visits
# print("Inserting patient visits...")
# for _ in tqdm(range(0, 376222, batch_size)):
#     visits_batch = []
#     for _ in range(batch_size):
#         # Biased list: repeat some IDs to increase frequency
#         frequent_patients = random.choices(patient_ids, k=len(patient_ids) // 10)
#         patient_pool = patient_ids + frequent_patients
#         patient_id = random.choice(patient_pool)

#         frequent_doctors = random.choices(doctor_ids, k=len(doctor_ids) // 10)
#         doctor_pool = doctor_ids + frequent_doctors
#         doctor_id = random.choice(doctor_pool)

#         department_id = random.choices(department_ids, weights=weights, k=1)[0]

#         common_diseases = disease_ids[:50]  # assume top 50 are common
#         disease_weights = [5 if disease_id in common_diseases else 1 for disease_id in disease_ids]
#         disease_id = random.choices(disease_ids, weights=disease_weights, k=1)[0]

        
#         month_weights = [3 if m in [1, 2, 6, 7, 11, 12] else 1 for m in range(1, 13)]
#         random_month = random.choices(range(1, 13), weights=month_weights, k=1)[0]
#         random_day = random.randint(1, 28)
#         random_year = random.choice([2023, 2024])
#         visit_date = f"{random_year}-{random_month:02}-{random_day:02}"

#         bed_occupied = random.choice([0, 1])
#         visits_batch.append((patient_id, doctor_id, department_id, disease_id, visit_date, bed_occupied))
#     cursor.executemany("""
#         INSERT INTO patient_visits (patient_id, doctor_id, department_id, disease_id, visit_date, bed_occupied)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """, visits_batch)
#     conn.commit()


# Close the connection
cursor.close()
conn.close()
print("Data insertion completed successfully.")
