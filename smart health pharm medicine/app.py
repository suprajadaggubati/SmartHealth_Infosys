from flask import Flask, render_template, request, redirect, session, jsonify, make_response
import sqlite3
import datetime
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = "smart_health_module1"

DB_NAME = "database.db"

# ---------------- DATABASE CONNECTION ----------------
def get_db():
    return sqlite3.connect(DB_NAME)

# ---------------- DATABASE INITIALIZATION ----------------
def init_db():
    con = get_db()
    cur = con.cursor()

    # User login table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Health profile table (Module 1)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS health_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        age INTEGER,
        gender TEXT,
        height REAL,
        weight REAL,
        activity TEXT,
        diseases TEXT,
        allergies TEXT,
        medicines TEXT
    )
    """)

    # ---------------- MODULE 2 : DIET & NUTRITION ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS diet_nutrition_dataset (
        food_id INTEGER PRIMARY KEY,
        food_name TEXT,
        category TEXT,
        calories INTEGER,
        protein INTEGER,
        carbs INTEGER,
        fats INTEGER,
        diet_type TEXT,
        recommended_time TEXT
    )
    """)

    # ---------------- MODULE 3 : SYMPTOM ANALYSIS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS symptom_medicine_dataset (
        symptom_id INTEGER PRIMARY KEY,
        symptom_name TEXT,
        severity TEXT,
        duration_days INTEGER,
        possible_condition TEXT,
        otc_medicine TEXT,
        medicine_type TEXT,
        dosage_info TEXT,
        doctor_consult TEXT,
        notes TEXT
    )
    """)

    # ---------------- MODULE 4 : MEDICINE REMINDER ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS medicine_reminder_dataset (
        medicine_id INTEGER PRIMARY KEY,
        medicine_name TEXT,
        dosage TEXT,
        frequency TEXT,
        duration_days INTEGER,
        reminder_time TEXT,
        medicine_type TEXT,
        interaction_warning TEXT
    )
    """)

    # ---------------- MODULE 4 : PHARMACY AVAILABILITY ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pharmacy_availability_dataset (
        pharmacy_id INTEGER PRIMARY KEY,
        pharmacy_name TEXT,
        location TEXT,
        medicine_name TEXT,
        stock TEXT,
        contact TEXT
    )
    """)

    # ---------------- MODULE 5 : DOCTOR CONSULTATION ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctor_consultation_dataset (
        doctor_id INTEGER PRIMARY KEY,
        doctor_name TEXT,
        specialization TEXT,
        hospital_name TEXT,
        location TEXT,
        contact TEXT,
        consultation_type TEXT,
        availability TEXT
    )
    """)

    # ---------------- MODULE 5 : HEALTH MONITORING ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS health_monitoring_dataset (
        record_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        weight REAL,
        symptom TEXT,
        severity TEXT,
        days_persisted INTEGER,
        doctor_alert TEXT,
        emergency_flag TEXT,
        remarks TEXT
    )
    """)

    con.commit()
    con.close()

# ---------------- INSERT DUMMY DATA ----------------
def insert_dummy_data():
    con = get_db()
    cur = con.cursor()

    # Dummy users
    dummy_users = [
        ("user1", "pass123"),
        ("user2", "pass456"),
        ("user3", "pass789"),
        ("user4", "passabc"),
        ("user5", "passxyz")
    ]
    for u in dummy_users:
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?,?)", u)
        except sqlite3.IntegrityError:
            pass  # skip if user exists

    # Dummy health profiles
    dummy_profiles = [
        (1, 25, 'Male', 175, 70, 'Moderate', 'None', 'Pollen', 'Vitamin D'),
        (2, 30, 'Female', 160, 60, 'Low', 'Diabetes', 'None', 'Metformin'),
        (3, 28, 'Male', 180, 80, 'High', 'Hypertension', 'Dust', 'Amlodipine'),
        (4, 22, 'Female', 165, 55, 'Moderate', 'None', 'None', 'Vitamin B12'),
        (5, 35, 'Male', 170, 75, 'Low', 'Asthma', 'Peanuts', 'Salbutamol')
    ]

    for p in dummy_profiles:
        # Check if user already has a profile
        cur.execute("SELECT * FROM health_profile WHERE user_id=?", (p[0],))
        if not cur.fetchone():
            cur.execute("""
                INSERT INTO health_profile
                (user_id, age, gender, height, weight, activity, diseases, allergies, medicines)
                VALUES (?,?,?,?,?,?,?,?,?)
            """, p)

    con.commit()
    con.close()
    print("Dummy data inserted successfully!")
 # ================= MODULE 2 =================
def insert_module2():
    con = get_db()
    cur = con.cursor()

    # Drop existing table if it has wrong structure
    cur.execute("DROP TABLE IF EXISTS module2_diet")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS module2_diet (
        id INTEGER PRIMARY KEY,
        food TEXT,
        calories INTEGER,
        protein INTEGER,
        carbs INTEGER,
        fats INTEGER,
        diet TEXT,
        meal TEXT,
        day TEXT
    )
    """)

    # Comprehensive data - At least 2 options per meal per day per diet type
    diet_data = [
        # MONDAY
        # Breakfast
        (1,'Idli with Sambar',120,4,22,1,'Diabetic','Breakfast','Monday'),
        (2,'Dosa',130,5,24,2,'Diabetic','Breakfast','Monday'),
        (3,'Poha',160,5,28,3,'Normal','Breakfast','Monday'),
        (4,'Upma',150,6,26,2,'Normal','Breakfast','Monday'),
        (5,'Oats Porridge',150,7,27,3,'Weight Loss','Breakfast','Monday'),
        (6,'Boiled Eggs',155,13,1,11,'Weight Loss','Breakfast','Monday'),
        (7,'Eggs',155,13,1,11,'Muscle Gain','Breakfast','Monday'),
        (8,'Egg Masala',180,14,5,12,'Muscle Gain','Breakfast','Monday'),
        # Lunch
        (9,'Roti with Dal',140,6,24,2,'Diabetic','Lunch','Monday'),
        (10,'Chapati with Veg',160,5,28,3,'Diabetic','Lunch','Monday'),
        (11,'Rice',200,4,45,1,'Normal','Lunch','Monday'),
        (12,'Pulao',220,5,42,4,'Normal','Lunch','Monday'),
        (13,'Mixed Veg with Roti',180,6,32,3,'Weight Loss','Lunch','Monday'),
        (14,'Salad Plate',95,4,10,1,'Weight Loss','Lunch','Monday'),
        (15,'Paneer',265,14,8,20,'Muscle Gain','Lunch','Monday'),
        (16,'Paneer Tikka',280,16,6,22,'Muscle Gain','Lunch','Monday'),
        # Snack
        (17,'Apple',95,0,25,0,'Diabetic','Snack','Monday'),
        (18,'Orange',80,1,19,0,'Diabetic','Snack','Monday'),
        (19,'Fruit Salad',95,2,24,0,'Weight Loss','Snack','Monday'),
        (20,'Sprouts',140,9,20,2,'Weight Loss','Snack','Monday'),
        (21,'Nuts',170,6,8,14,'Muscle Gain','Snack','Monday'),
        (22,'Almonds',180,7,6,16,'Muscle Gain','Snack','Monday'),
        (23,'Milk',130,8,12,5,'Normal','Snack','Monday'),
        (24,'Banana',105,1,27,0,'Normal','Snack','Monday'),
        # Dinner
        (25,'Vegetable Soup',80,3,12,1,'Diabetic','Dinner','Monday'),
        (26,'Tomato Soup',90,3,14,2,'Diabetic','Dinner','Monday'),
        (27,'Chapati with Veg Curry',220,6,40,4,'Normal','Dinner','Monday'),
        (28,'Rice with Dal',210,7,38,3,'Normal','Dinner','Monday'),
        (29,'Salad with Grilled Fish',140,18,8,5,'Weight Loss','Dinner','Monday'),
        (30,'Steamed Broccoli',110,8,18,2,'Weight Loss','Dinner','Monday'),
        (31,'Grilled Paneer',240,18,6,18,'Muscle Gain','Dinner','Monday'),
        (32,'Grilled Chicken Breast',260,35,2,12,'Muscle Gain','Dinner','Monday'),
        
        # TUESDAY
        # Breakfast
        (33,'Avial',140,5,24,3,'Diabetic','Breakfast','Tuesday'),
        (34,'Appam',110,3,20,2,'Diabetic','Breakfast','Tuesday'),
        (35,'Pongal',190,6,34,4,'Normal','Breakfast','Tuesday'),
        (36,'Uttapam',180,6,32,4,'Normal','Breakfast','Tuesday'),
        (37,'Cornflakes',170,4,32,2,'Weight Loss','Breakfast','Tuesday'),
        (38,'Multigrain Toast',140,6,22,3,'Weight Loss','Breakfast','Tuesday'),
        (39,'Cottage Cheese Omelet',160,14,2,10,'Muscle Gain','Breakfast','Tuesday'),
        (40,'Scrambled Eggs',150,12,3,10,'Muscle Gain','Breakfast','Tuesday'),
        # Lunch
        (41,'Bhindi Fry with Roti',130,4,20,4,'Diabetic','Lunch','Tuesday'),
        (42,'Bitter Gourd with Dal',120,5,18,2,'Diabetic','Lunch','Tuesday'),
        (43,'Veg Biryani',290,6,52,8,'Normal','Lunch','Tuesday'),
        (44,'Fish Curry',250,24,2,10,'Normal','Lunch','Tuesday'),
        (45,'Stir Fry Vegetables',110,5,16,3,'Weight Loss','Lunch','Tuesday'),
        (46,'Grilled Tofu',120,16,6,5,'Weight Loss','Lunch','Tuesday'),
        (47,'Chicken Curry',280,26,4,12,'Muscle Gain','Lunch','Tuesday'),
        (48,'Egg Curry',260,20,4,18,'Muscle Gain','Lunch','Tuesday'),
        # Snack
        (49,'Watermelon',70,1,18,0,'Diabetic','Snack','Tuesday'),
        (50,'Papaya',85,1,21,0,'Diabetic','Snack','Tuesday'),
        (51,'Cucumber',45,2,8,0,'Weight Loss','Snack','Tuesday'),
        (52,'Carrots',60,1,14,0,'Weight Loss','Snack','Tuesday'),
        (53,'Mixed Dry Fruits',200,7,18,12,'Muscle Gain','Snack','Tuesday'),
        (54,'Peanuts',160,7,6,14,'Muscle Gain','Snack','Tuesday'),
        (55,'Curd',90,5,6,3,'Normal','Snack','Tuesday'),
        (56,'Buttermilk',60,3,5,1,'Normal','Snack','Tuesday'),
        # Dinner
        (57,'Dal with Roti',140,6,24,2,'Diabetic','Dinner','Tuesday'),
        (58,'Moong Dal Soup',110,8,16,1,'Diabetic','Dinner','Tuesday'),
        (59,'Khichdi',200,7,35,4,'Normal','Dinner','Tuesday'),
        (60,'Veg Pulao',240,6,44,6,'Normal','Dinner','Tuesday'),
        (61,'Baked Vegetables',100,4,18,2,'Weight Loss','Dinner','Tuesday'),
        (62,'Steamed Fish',150,24,1,6,'Weight Loss','Dinner','Tuesday'),
        (63,'Paneer Butter Masala',290,18,12,20,'Muscle Gain','Dinner','Tuesday'),
        (64,'Chicken Tikka Masala',310,32,8,18,'Muscle Gain','Dinner','Tuesday'),
        
        # WEDNESDAY
        # Breakfast
        (65,'Chikhalwali',150,5,26,2,'Diabetic','Breakfast','Wednesday'),
        (66,'Puttu',140,4,25,2,'Diabetic','Breakfast','Wednesday'),
        (67,'Idiyappam',160,4,30,1,'Normal','Breakfast','Wednesday'),
        (68,'Paratha',210,6,36,6,'Normal','Breakfast','Wednesday'),
        (69,'Brown Bread Toast',130,5,20,3,'Weight Loss','Breakfast','Wednesday'),
        (70,'Oat Bran Cereal',140,6,24,2,'Weight Loss','Breakfast','Wednesday'),
        (71,'Omelets',160,14,2,11,'Muscle Gain','Breakfast','Wednesday'),
        (72,'Protein Pancakes',180,15,20,6,'Muscle Gain','Breakfast','Wednesday'),
        # Lunch
        (73,'Brinjal Fry with Roti',150,4,26,4,'Diabetic','Lunch','Wednesday'),
        (74,'Okra Curry',120,3,18,4,'Diabetic','Lunch','Wednesday'),
        (75,'Tomato Rice',180,4,40,2,'Normal','Lunch','Wednesday'),
        (76,'Burger',320,14,40,15,'Normal','Lunch','Wednesday'),
        (77,'Green Beans',85,4,12,1,'Weight Loss','Lunch','Wednesday'),
        (78,'Soup with Salad',100,5,12,2,'Weight Loss','Lunch','Wednesday'),
        (79,'Fish Fry',270,28,2,14,'Muscle Gain','Lunch','Wednesday'),
        (80,'Mutton Curry',300,32,2,16,'Muscle Gain','Lunch','Wednesday'),
        # Snack
        (81,'Guava',110,2,23,1,'Diabetic','Snack','Wednesday'),
        (82,'Pomegranate',80,2,18,1,'Diabetic','Snack','Wednesday'),
        (83,'Beetroot',70,2,16,0,'Weight Loss','Snack','Wednesday'),
        (84,'Radish',30,1,6,0,'Weight Loss','Snack','Wednesday'),
        (85,'Walnuts',180,4,8,18,'Muscle Gain','Snack','Wednesday'),
        (86,'Cashews',160,5,9,13,'Muscle Gain','Snack','Wednesday'),
        (87,'Yogurt',100,6,8,3,'Normal','Snack','Wednesday'),
        (88,'Flavored Milk',130,7,14,4,'Normal','Snack','Wednesday'),
        # Dinner
        (89,'Mung Bean Soup',130,10,18,1,'Diabetic','Dinner','Wednesday'),
        (90,'Lentil Stew',140,11,20,2,'Diabetic','Dinner','Wednesday'),
        (91,'Coconut Rice',220,4,44,4,'Normal','Dinner','Wednesday'),
        (92,'Prawn Curry',240,26,4,14,'Normal','Dinner','Wednesday'),
        (93,'Steamed Veggies',90,5,16,1,'Weight Loss','Dinner','Wednesday'),
        (94,'Grilled Salmon',200,24,1,11,'Weight Loss','Dinner','Wednesday'),
        (95,'Tandoori Chicken',280,36,2,14,'Muscle Gain','Dinner','Wednesday'),
        (96,'Grilled Steak',300,38,1,16,'Muscle Gain','Dinner','Wednesday'),
        
        # THURSDAY
        # Breakfast
        (97,'Puttu Kuzhambhu',160,5,28,2,'Diabetic','Breakfast','Thursday'),
        (98,'Suji Upma',140,5,25,2,'Diabetic','Breakfast','Thursday'),
        (99,'Paratha',210,6,36,6,'Normal','Breakfast','Thursday'),
        (100,'Puri',180,5,32,5,'Normal','Breakfast','Thursday'),
        (101,'Granola',160,6,26,4,'Weight Loss','Breakfast','Thursday'),
        (102,'Chia Pudding',140,8,16,6,'Weight Loss','Breakfast','Thursday'),
        (103,'Boiled Eggs with Toast',170,14,16,8,'Muscle Gain','Breakfast','Thursday'),
        (104,'Smoked Salmon',180,22,2,10,'Muscle Gain','Breakfast','Thursday'),
        # Lunch
        (105,'Bitter Gourd Curry',110,3,18,3,'Diabetic','Lunch','Thursday'),
        (106,'Pumpkin Fry',100,2,20,1,'Diabetic','Lunch','Thursday'),
        (107,'Veg Fried Rice',200,5,40,4,'Normal','Lunch','Thursday'),
        (108,'Shrimp Biryani',280,24,48,8,'Normal','Lunch','Thursday'),
        (109,'Raw Vegetable Plate',70,3,12,1,'Weight Loss','Lunch','Thursday'),
        (110,'Baked Tofu',130,16,8,5,'Weight Loss','Lunch','Thursday'),
        (111,'Roast Chicken',270,34,1,14,'Muscle Gain','Lunch','Thursday'),
        (112,'Kebab',290,32,4,16,'Muscle Gain','Lunch','Thursday'),
        # Snack
        (113,'Mango',80,1,20,0,'Diabetic','Snack','Thursday'),
        (114,'Peach',60,1,14,0,'Diabetic','Snack','Thursday'),
        (115,'Raw Spinach',30,3,4,0,'Weight Loss','Snack','Thursday'),
        (116,'Mushrooms',25,2,3,0,'Weight Loss','Snack','Thursday'),
        (117,'Brazil Nuts',190,4,3,19,'Muscle Gain','Snack','Thursday'),
        (118,'Macadamia Nuts',200,2,4,21,'Muscle Gain','Snack','Thursday'),
        (119,'Lassi',120,6,12,4,'Normal','Snack','Thursday'),
        (120,'Fruit Smoothie',150,4,28,2,'Normal','Snack','Thursday'),
        # Dinner
        (121,'Corn Soup',110,4,20,2,'Diabetic','Dinner','Thursday'),
        (122,'Vegetable Stew',100,3,18,1,'Diabetic','Dinner','Thursday'),
        (123,'Egg Fried Rice',250,9,44,7,'Normal','Dinner','Thursday'),
        (124,'Noodles',310,10,46,12,'Normal','Dinner','Thursday'),
        (125,'Zucchini Noodles',60,2,12,1,'Weight Loss','Dinner','Thursday'),
        (126,'Seabass',170,28,1,6,'Weight Loss','Dinner','Thursday'),
        (127,'Lamb Curry',320,34,6,18,'Muscle Gain','Dinner','Thursday'),
        (128,'Spiced Chicken',290,32,4,16,'Muscle Gain','Dinner','Thursday'),
        
        # FRIDAY
        # Breakfast
        (129,'Poha',160,5,28,3,'Diabetic','Breakfast','Friday'),
        (130,'Falafel',150,6,20,6,'Diabetic','Breakfast','Friday'),
        (131,'Cornflakes',170,4,32,2,'Normal','Breakfast','Friday'),
        (132,'Toast',140,5,22,3,'Normal','Breakfast','Friday'),
        (133,'Low-Fat Yogurt',90,10,6,1,'Weight Loss','Breakfast','Friday'),
        (134,'Protein Shake',140,20,8,2,'Weight Loss','Breakfast','Friday'),
        (135,'Egg White Omelet',120,16,2,4,'Muscle Gain','Breakfast','Friday'),
        (136,'Steak with Eggs',300,32,4,16,'Muscle Gain','Breakfast','Friday'),
        # Lunch
        (137,'Snake Gourd Curry',100,2,18,2,'Diabetic','Lunch','Friday'),
        (138,'Bottle Gourd Dal',110,7,16,2,'Diabetic','Lunch','Friday'),
        (139,'Fried Rice',200,6,40,3,'Normal','Lunch','Friday'),
        (140,'Pizza',350,16,42,18,'Normal','Lunch','Friday'),
        (141,'Lettuce Wraps',80,5,10,2,'Weight Loss','Lunch','Friday'),
        (142,'Baked Chicken Breast',200,32,2,8,'Weight Loss','Lunch','Friday'),
        (143,'Butter Chicken',310,26,8,20,'Muscle Gain','Lunch','Friday'),
        (144,'Tikka Masala',300,28,12,16,'Muscle Gain','Lunch','Friday'),
        # Snack
        (145,'Pineapple',80,1,20,0,'Diabetic','Snack','Friday'),
        (146,'Grapes',80,1,20,0,'Diabetic','Snack','Friday'),
        (147,'Celery',20,1,4,0,'Weight Loss','Snack','Friday'),
        (148,'Tomato',25,1,5,0,'Weight Loss','Snack','Friday'),
        (149,'Pistachio',160,6,8,14,'Muscle Gain','Snack','Friday'),
        (150,'Sunflower Seeds',180,6,8,16,'Muscle Gain','Snack','Friday'),
        (151,'Coconut Water',50,1,12,0,'Normal','Snack','Friday'),
        (152,'Ice Cream',210,4,28,11,'Normal','Snack','Friday'),
        # Dinner
        (153,'Pea Soup',100,8,14,1,'Diabetic','Dinner','Friday'),
        (154,'Bean Stew',120,9,16,2,'Diabetic','Dinner','Friday'),
        (155,'Vegetable Pasta',280,10,48,6,'Normal','Dinner','Friday'),
        (156,'Seafood Pasta',320,28,42,10,'Normal','Dinner','Friday'),
        (157,'Grilled Vegetables',95,4,18,2,'Weight Loss','Dinner','Friday'),
        (158,'White Fish',160,26,1,6,'Weight Loss','Dinner','Friday'),
        (159,'Kabab with Rice',340,36,28,14,'Muscle Gain','Dinner','Friday'),
        (160,'Biryani',350,28,48,12,'Muscle Gain','Dinner','Friday'),
        
        # SATURDAY
        # Breakfast
        (161,'Dosa with Chutney',168,5,30,3,'Diabetic','Breakfast','Saturday'),
        (162,'Idli',120,4,22,1,'Diabetic','Breakfast','Saturday'),
        (163,'Vada',160,6,22,6,'Normal','Breakfast','Saturday'),
        (164,'Sandwich',220,8,34,6,'Normal','Breakfast','Saturday'),
        (165,'Protein Pancakes',180,15,20,6,'Weight Loss','Breakfast','Saturday'),
        (166,'Greek Yogurt Bowl',120,15,12,2,'Weight Loss','Breakfast','Saturday'),
        (167,'Beef Steak',350,42,2,20,'Muscle Gain','Breakfast','Saturday'),
        (168,'Smoked Salmon Bagel',280,18,32,12,'Muscle Gain','Breakfast','Saturday'),
        # Lunch
        (169,'Cluster Beans',130,6,18,3,'Diabetic','Lunch','Saturday'),
        (170,'Capsicum Fry',110,3,18,3,'Diabetic','Lunch','Saturday'),
        (171,'Crab Fried Rice',290,24,40,8,'Normal','Lunch','Saturday'),
        (172,'Mutton Biryani',320,30,44,12,'Normal','Lunch','Saturday'),
        (173,'Sprouted Beans',140,12,18,2,'Weight Loss','Lunch','Saturday'),
        (174,'Baked Cod',180,30,2,6,'Weight Loss','Lunch','Saturday'),
        (175,'Prime Rib',380,40,2,24,'Muscle Gain','Lunch','Saturday'),
        (176,'Grilled Duck',340,36,2,20,'Muscle Gain','Lunch','Saturday'),
        # Snack
        (177,'Plum',80,1,19,0,'Diabetic','Snack','Saturday'),
        (178,'Kiwi',60,1,14,0,'Diabetic','Snack','Saturday'),
        (179,'Green Bell Pepper',40,1,8,0,'Weight Loss','Snack','Saturday'),
        (180,'Onion',40,1,9,0,'Weight Loss','Snack','Saturday'),
        (181,'Pecan Nuts',190,3,4,19,'Muscle Gain','Snack','Saturday'),
        (182,'Pine Nuts',190,4,4,19,'Muscle Gain','Snack','Saturday'),
        (183,'Condensed Milk',140,3,24,4,'Normal','Snack','Saturday'),
        (184,'Dark Chocolate',180,3,22,10,'Normal','Snack','Saturday'),
        # Dinner
        (185,'Carrot Soup',90,3,16,1,'Diabetic','Dinner','Saturday'),
        (186,'Spinach Soup',100,5,14,2,'Diabetic','Dinner','Saturday'),
        (187,'Vegetable Lo Mein',240,6,44,6,'Normal','Dinner','Saturday'),
        (188,'Shrimp Lo Mein',280,22,42,8,'Normal','Dinner','Saturday'),
        (189,'Cauliflower Rice',70,3,12,1,'Weight Loss','Dinner','Saturday'),
        (190,'Grilled Shrimp',160,28,2,5,'Weight Loss','Dinner','Saturday'),
        (191,'Lamb Chops',360,38,2,22,'Muscle Gain','Dinner','Saturday'),
        (192,'Grilled Fish Steak',250,34,1,12,'Muscle Gain','Dinner','Saturday'),
        
        # SUNDAY
        # Breakfast
        (193,'Pongal',190,6,34,4,'Diabetic','Breakfast','Sunday'),
        (194,'Uttapam',180,6,32,4,'Diabetic','Breakfast','Sunday'),
        (195,'Bagel',220,8,40,4,'Normal','Breakfast','Sunday'),
        (196,'Crepes',200,6,38,4,'Normal','Breakfast','Sunday'),
        (197,'Tofu Scramble',140,16,10,5,'Weight Loss','Breakfast','Sunday'),
        (198,'Berry Smoothie Bowl',160,8,28,3,'Weight Loss','Breakfast','Sunday'),
        (199,'Turkey Sausage',200,24,2,12,'Muscle Gain','Breakfast','Sunday'),
        (200,'Canadian Bacon',190,20,1,11,'Muscle Gain','Breakfast','Sunday'),
        # Lunch
        (201,'Fenugreek Leaves Curry',110,5,16,3,'Diabetic','Lunch','Sunday'),
        (202,'Coriander Leaves Curry',100,4,14,2,'Diabetic','Lunch','Sunday'),
        (203,'Chow Mein',310,10,50,8,'Normal','Lunch','Sunday'),
        (204,'Hakka Noodles',300,8,48,8,'Normal','Lunch','Sunday'),
        (205,'Quinoa Bowl',180,8,32,4,'Weight Loss','Lunch','Sunday'),
        (206,'Lentil Salad',150,12,20,3,'Weight Loss','Lunch','Sunday'),
        (207,'Roasted Turkey',280,38,2,12,'Muscle Gain','Lunch','Sunday'),
        (208,'Veal Chop',310,36,2,18,'Muscle Gain','Lunch','Sunday'),
        # Snack
        (209,'Blueberry',80,1,20,0,'Diabetic','Snack','Sunday'),
        (210,'Strawberry',50,1,12,0,'Diabetic','Snack','Sunday'),
        (211,'Cabbage',25,1,6,0,'Weight Loss','Snack','Sunday'),
        (212,'Pumpkin',40,1,9,0,'Weight Loss','Snack','Sunday'),
        (213,'Hazelnut',180,4,5,17,'Muscle Gain','Snack','Sunday'),
        (214,'Chestnut',140,2,28,1,'Muscle Gain','Snack','Sunday'),
        (215,'Almond Milk',30,1,1,2,'Normal','Snack','Sunday'),
        (216,'Dried Fruit Mix',200,4,48,2,'Normal','Snack','Sunday'),
        # Dinner
        (217,'Bottle Gourd Soup',85,2,14,1,'Diabetic','Dinner','Sunday'),
        (218,'Ash Gourd Soup',80,2,12,1,'Diabetic','Dinner','Sunday'),
        (219,'Chicken Fried Rice',330,14,50,8,'Normal','Dinner','Sunday'),
        (220,'Vegetable Fried Rice',240,6,46,4,'Normal','Dinner','Sunday'),
        (221,'Steamed Broccoli Rice',120,8,20,2,'Weight Loss','Dinner','Sunday'),
        (222,'Baked Halibut',200,28,2,10,'Weight Loss','Dinner','Sunday'),
        (223,'BBQ Ribs',400,32,20,24,'Muscle Gain','Dinner','Sunday'),
        (224,'Grilled Pork Chop',340,40,2,18,'Muscle Gain','Dinner','Sunday'),
    ]

    cur.executemany("INSERT OR IGNORE INTO module2_diet VALUES (?,?,?,?,?,?,?,?,?)", diet_data)
    con.commit()
    con.close()

def insert_module3():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS module3_symptoms (
        id INTEGER PRIMARY KEY,
        symptom TEXT,
        severity TEXT,
        days INTEGER,
        condition TEXT,
        medicine TEXT,
        consult TEXT
    )
    """)

    cur.executemany("INSERT OR IGNORE INTO module3_symptoms VALUES (?,?,?,?,?,?,?)", [
        (1,'Fever','Mild',2,'Viral','Paracetamol','No'),
        (2,'Cold','Mild',3,'Flu','Cetirizine','No'),
        (3,'Headache','Moderate',2,'Migraine','Ibuprofen','No'),
        (4,'Cough','Mild',4,'Cold','Cough Syrup','No'),
        (5,'Chest Pain','Severe',1,'Cardiac','None','Yes'),
        (6,'Stomach Pain','Moderate',2,'Gastritis','Antacid','Yes'),
        (7,'Vomiting','Moderate',1,'Food Poison','ORS','Yes'),
        (8,'Diarrhea','Moderate',2,'Infection','ORS','Yes'),
        (9,'Breathing Issue','Severe',1,'Asthma','Inhaler','Yes'),
        (10,'Body Pain','Moderate',3,'Fatigue','Pain Killer','No'),
        (11,'Back Pain','Moderate',5,'Muscle Strain','Pain Relief','No'),
        (12,'Joint Pain','Moderate',4,'Arthritis','Pain Relief','Yes'),
        (13,'Eye Irritation','Mild',2,'Allergy','Eye Drops','No'),
        (14,'Ear Pain','Moderate',3,'Infection','Antibiotic','Yes'),
        (15,'Toothache','Severe',2,'Dental Issue','Pain Relief','Yes'),
        (16,'Skin Rash','Mild',3,'Allergy','Antihistamine','No'),
        (17,'Burning Urine','Moderate',2,'UTI','Antibiotic','Yes'),
        (18,'Nausea','Mild',1,'Indigestion','Antacid','No'),
        (19,'Loss of Appetite','Mild',4,'Weakness','Vitamins','No'),
        (20,'Fainting','Severe',1,'Low BP','None','Yes'),
        (21,'Sneezing','Mild',2,'Allergy','Cetirizine','No'),
        (22,'Runny Nose','Mild',3,'Cold','Antihistamine','No'),
        (23,'High BP','Severe',5,'Hypertension','BP Medicine','Yes'),
        (24,'Low BP','Moderate',3,'Hypotension','Fluids','Yes'),
        (25,'Sugar Fluctuation','Severe',4,'Diabetes','Insulin','Yes'),
        (26,'Constipation','Mild',5,'Digestion','Fiber','No'),
        (27,'Gas','Mild',2,'Indigestion','Antacid','No'),
        (28,'Acidity','Moderate',3,'Gastric','Antacid','No'),
        (29,'Hair Fall','Mild',10,'Deficiency','Vitamins','No'),
        (30,'Dizziness','Moderate',2,'Vertigo','Medication','Yes'),
        (31,'Sleep Issues','Mild',7,'Insomnia','Supplements','No'),
        (32,'Depression','Severe',14,'Mental Health','None','Yes'),
        (33,'Anxiety','Moderate',10,'Stress','Relaxants','Yes'),
        (34,'Memory Loss','Moderate',15,'Cognitive','Supplements','Yes'),
        (35,'Leg Pain','Moderate',4,'Muscle','Pain Relief','No'),
        (36,'Neck Pain','Moderate',3,'Strain','Pain Relief','No'),
        (37,'Swelling','Moderate',2,'Inflammation','Pain Relief','Yes'),
        (38,'Itching','Mild',2,'Allergy','Antihistamine','No'),
        (39,'Red Eyes','Mild',1,'Irritation','Eye Drops','No'),
        (40,'Blur Vision','Severe',1,'Eye Issue','None','Yes'),
        (41,'Heartburn','Mild',2,'Acidity','Antacid','No'),
        (42,'Ulcer Pain','Severe',5,'Ulcer','Medication','Yes'),
        (43,'Cold Sweats','Severe',1,'Shock','None','Yes'),
        (44,'Weakness','Mild',6,'Fatigue','Vitamins','No'),
        (45,'Weight Loss','Moderate',30,'Metabolic','Supplements','Yes'),
        (46,'Weight Gain','Moderate',30,'Lifestyle','Diet Plan','No'),
        (47,'Fever with Chills','Severe',3,'Malaria','Antimalarial','Yes'),
        (48,'Cramps','Mild',2,'Muscle','Pain Relief','No'),
        (49,'Numbness','Moderate',4,'Nerve Issue','Supplements','Yes'),
        (50,'Palpitations','Severe',1,'Cardiac','None','Yes')

    ])
	
    con.commit()
    con.close()
def insert_module4():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS module4_medicines (
        id INTEGER PRIMARY KEY,
        name TEXT,
        dosage TEXT,
        frequency TEXT,
        duration INTEGER,
        warning TEXT
    )
    """)

    cur.executemany("INSERT OR IGNORE INTO module4_medicines VALUES (?,?,?,?,?,?)", [
        (1,'Paracetamol','500mg','2 times',3,'Avoid overdose'),
        (2,'Ibuprofen','400mg','2 times',3,'After food'),
        (3,'Cetirizine','10mg','Once',5,'Drowsiness'),
        (4,'Antacid','10ml','2 times',7,'Before meals'),
        (5,'ORS','1 packet','As needed',2,'Drink slowly'),
        (6,'Vitamin C','500mg','Once',10,'None'),
        (7,'Vitamin D','60000IU','Weekly',8,'Once a week'),
        (8,'Calcium','500mg','Once',30,'After food'),
        (9,'BP Tablet','5mg','Once',30,'Daily'),
        (10,'Sugar Tablet','10mg','Once',30,'Monitor sugar'),
        (11,'Insulin','As advised','Daily',30,'Doctor advice'),
        (12,'Pain Relief','650mg','2 times',5,'Avoid empty stomach'),
        (13,'Antibiotic','500mg','3 times',7,'Complete course'),
        (14,'Eye Drops','2 drops','3 times',5,'Clean hands'),
        (15,'Ear Drops','2 drops','2 times',5,'Warm bottle'),
        (16,'Cough Syrup','10ml','3 times',5,'Shake well'),
        (17,'Asthma Inhaler','2 puffs','As needed',30,'Correct usage'),
        (18,'Thyroid Tablet','50mcg','Once',30,'Morning'),
        (19,'Iron Tablet','100mg','Once',30,'After food'),
        (20,'Zinc Tablet','50mg','Once',15,'After meals'),
        (21,'Antiallergic','10mg','Once',7,'Drowsy'),
        (22,'Digestive','1 cap','Once',10,'Before food'),
        (23,'Laxative','10ml','Once',5,'Night'),
        (24,'Antifungal','1 tab','Once',14,'Complete course'),
        (25,'Antiviral','1 tab','2 times',7,'Doctor advice'),
        (26,'Pain Gel','Apply','2 times',5,'External only'),
        (27,'Cold Tablet','1 tab','2 times',3,'After food'),
        (28,'Fever Syrup','10ml','3 times',3,'Check temp'),
        (29,'BP Syrup','10ml','Once',30,'Daily'),
        (30,'Multivitamin','1 tab','Once',30,'Daily'),
        (31,'Protein Powder','1 scoop','Once',30,'With milk'),
        (32,'Electrolyte','1 sachet','Once',2,'With water'),
        (33,'Anti-nausea','1 tab','2 times',3,'As needed'),
        (34,'Acid Control','1 tab','Once',14,'Before food'),
        (35,'Heart Tablet','1 tab','Once',30,'Monitor BP'),
        (36,'Sedative','1 tab','Night',7,'Avoid driving'),
        (37,'Pain Injection','As advised','Once',1,'Doctor only'),
        (38,'Antiseptic','Apply','2 times',7,'External'),
        (39,'Burn Ointment','Apply','2 times',5,'External'),
        (40,'Worm Tablet','1 tab','Once',1,'Yearly'),
        (41,'Anti TB','As advised','Daily',180,'Strict'),
        (42,'Cholesterol','10mg','Once',30,'Night'),
        (43,'Steroid','5mg','Once',10,'Doctor advice'),
        (44,'Eye Vitamin','1 cap','Once',30,'Daily'),
        (45,'Joint Tablet','1 tab','Once',30,'After food'),
        (46,'Sleep Aid','1 tab','Night',7,'Short term'),
        (47,'Mood Tablet','1 tab','Once',14,'Doctor'),
        (48,'Pain Spray','Spray','As needed',7,'External'),
        (49,'Anti-gas','1 tab','Once',5,'After food'),
        (50,'Anti-diarrheal','1 tab','2 times',3,'Hydration')
    ])

    con.commit()
    con.close()
def insert_module5():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS module5_doctors (
        id INTEGER PRIMARY KEY,
        doctor TEXT,
        specialization TEXT,
        hospital TEXT,
        availability TEXT
    )
    """)

    cur.executemany("INSERT OR IGNORE INTO module5_doctors VALUES (?,?,?,?,?)", [
        (1,'Dr Ravi','Physician','City Hospital','Available'),
        (2,'Dr Kumar','Cardiologist','Apollo','Busy'),
        (3,'Dr Anitha','ENT','Care','Available'),
        (4,'Dr Suresh','Neurologist','Yashoda','Available'),
        (5,'Dr Meena','Gynecologist','Rainbow','Available'),
        (6,'Dr Ramesh','Orthopedic','KIMS','Busy'),
        (7,'Dr Sunil','Dermatologist','Aster','Available'),
        (8,'Dr Kavya','Psychiatrist','Fortis','Available'),
        (9,'Dr Mohan','Pediatrician','Cloudnine','Available'),
        (10,'Dr Sneha','General','City Hospital','Busy'),
        (11,'Dr Arjun','Urologist','Apollo','Available'),
        (12,'Dr Neelima','Dentist','Smile Care','Available'),
        (13,'Dr Kiran','Eye','LV Prasad','Available'),
        (14,'Dr Suman','ENT','Care','Busy'),
        (15,'Dr Divya','Physician','Govt Hospital','Available'),
        (16,'Dr Prasad','Cardio','Yashoda','Busy'),
        (17,'Dr Teja','Neuro','Aster','Available'),
        (18,'Dr Nikhil','General','City Hospital','Available'),
        (19,'Dr Latha','Gynec','Rainbow','Busy'),
        (20,'Dr Vinod','Physician','KIMS','Available'),
        (21,'Dr Ajay','Orthopedic','Apollo','Available'),
        (22,'Dr Sruthi','Dermatology','Care','Available'),
        (23,'Dr Raju','General','Govt','Busy'),
        (24,'Dr Pooja','Pediatric','Cloudnine','Available'),
        (25,'Dr Manohar','ENT','Aster','Available'),
        (26,'Dr Sai','Cardio','Apollo','Busy'),
        (27,'Dr Harsha','Psychiatry','Fortis','Available'),
        (28,'Dr Bhavya','Eye','LV Prasad','Available'),
        (29,'Dr Deepak','General','City','Available'),
        (30,'Dr Swathi','Gynec','Rainbow','Busy'),
        (31,'Dr Mahesh','Neuro','Yashoda','Available'),
        (32,'Dr Keerthi','Dermatology','Care','Available'),
        (33,'Dr Anand','Urology','Apollo','Busy'),
        (34,'Dr Lakshmi','Physician','Govt','Available'),
        (35,'Dr Sanjay','Orthopedic','KIMS','Available'),
        (36,'Dr Rina','Dentist','Smile Care','Busy'),
        (37,'Dr Akhil','General','City','Available'),
        (38,'Dr Varun','ENT','Aster','Available'),
        (39,'Dr Jyothi','Pediatric','Cloudnine','Busy'),
        (40,'Dr Naveen','Cardio','Apollo','Available'),
        (41,'Dr Srilatha','Gynec','Rainbow','Available'),
        (42,'Dr Rohit','Neuro','Care','Busy'),
        (43,'Dr Karthik','General','City','Available'),
        (44,'Dr Monica','Dermatology','Aster','Available'),
        (45,'Dr Bala','Physician','Govt','Busy'),
        (46,'Dr Shilpa','Eye','LV Prasad','Available'),
        (47,'Dr Chandu','ENT','Care','Available'),
        (48,'Dr Vamsi','Orthopedic','Apollo','Busy'),
        (49,'Dr Rekha','General','City','Available'),
        (50,'Dr Tarun','Cardiology','Yashoda','Available')
    ])

    con.commit()
    con.close()

# Initialize DB and dummy data
init_db()
insert_dummy_data()
insert_module2()
insert_module3()
insert_module4()
insert_module5()


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = get_db()
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?,?)",
                (username, password)
            )
            con.commit()
        except:
            pass
        con.close()
        return redirect("/login")

    return render_template("register.html")

# ================== API ROUTES (AJAX) ==================
@app.route("/api/register", methods=["POST"])
def api_register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"success": False, "message": "Username and password required"})
    
    con = get_db()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        con.close()
        return jsonify({"success": True, "message": "Registration successful"})
    except sqlite3.IntegrityError:
        con.close()
        return jsonify({"success": False, "message": "Username already exists"})
    except Exception as e:
        con.close()
        return jsonify({"success": False, "message": str(e)})

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    con.close()
    
    if user:
        session["user_id"] = user[0]
        session["username"] = username
        return jsonify({"success": True, "user_id": user[0], "username": username, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Incorrect username or password"})

# ================== FORM-BASED LOGIN (LEGACY) ==================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = get_db()
        cur = con.cursor()
        cur.execute(
            "SELECT id FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = cur.fetchone()
        con.close()

        if user:
            session["user_id"] = user[0]
            return redirect("/profile")

    return render_template("login.html")

# ---------------- HEALTH PROFILE ----------------
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        return redirect("/login")

    con = get_db()
    cur = con.cursor()
    
    # Fetch existing profile data
    cur.execute("""
    SELECT age, gender, height, weight, activity, diseases, allergies, medicines
    FROM health_profile
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT 1
    """, (session["user_id"],))
    
    existing_data = cur.fetchone()
    con.close()

    if request.method == "POST":
        data = (
            session["user_id"],
            request.form["age"],
            request.form["gender"],
            request.form["height"],
            request.form["weight"],
            request.form["activity"],
            request.form["diseases"] if request.form["diseases"] else "",
            request.form["allergies"] if request.form["allergies"] else "",
            request.form["medicines"] if request.form["medicines"] else ""
        )

        con = get_db()
        
        # If profile exists, update it; otherwise create new one
        if existing_data:
            con.execute("""
            UPDATE health_profile
            SET age=?, gender=?, height=?, weight=?, activity=?, diseases=?, allergies=?, medicines=?
            WHERE user_id=?
            """, (request.form["age"], request.form["gender"], request.form["height"], 
                  request.form["weight"], request.form["activity"], 
                  request.form["diseases"] if request.form["diseases"] else "",
                  request.form["allergies"] if request.form["allergies"] else "",
                  request.form["medicines"] if request.form["medicines"] else "",
                  session["user_id"]))
        else:
            con.execute("""
            INSERT INTO health_profile
            (user_id, age, gender, height, weight, activity, diseases, allergies, medicines)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, data)
        
        con.commit()
        con.close()

        return redirect("/dashboard")

    return render_template("profile.html", profile_data=existing_data)

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    con = get_db()
    cur = con.cursor()
    cur.execute("""
    SELECT age, gender, height, weight, activity, diseases, allergies, medicines
    FROM health_profile
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT 1
    """, (session["user_id"],))

    data = cur.fetchone()
    con.close()

    return render_template("dashboard.html", data=data)
# ================= MODULE 2 HELPERS =================

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m * height_m), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_daily_calories(weight, activity):
    if activity == "Low":
        return int(weight * 25)
    elif activity == "Moderate":
        return int(weight * 30)
    else:
        return int(weight * 35)


def decide_diet_type(bmi, diseases):
    if diseases and "Diabetes" in diseases:
        return "Diabetic"
    elif bmi >= 25:
        return "Weight Loss"
    elif bmi < 18.5:
        return "Muscle Gain"
    else:
        return "Normal"


# ================= MODULE 2 : DIET & NUTRITION =================


@app.route("/diet", methods=["GET", "POST"])
def diet():
    if "user_id" not in session:
        return redirect("/login")

    # Handle satisfaction response
    if request.method == "POST":
        satisfaction = request.form.get("satisfaction")
        if satisfaction == "yes":
            return redirect("/diet?success=Diet+plan+saved+successfully")
        elif satisfaction == "no":
            # Recreate diet plan by refreshing with timestamp for cache busting
            import time
            return redirect(f"/diet?regenerate=true&t={int(time.time())}")

    con = get_db()
    cur = con.cursor()

    # Fetch Latest Health Profile
    cur.execute("""
        SELECT weight, height, activity, diseases, age, gender
        FROM health_profile
        WHERE user_id=?
        ORDER BY id DESC LIMIT 1
    """, (session["user_id"],))

    profile = cur.fetchone()
    if not profile:
        con.close()
        return redirect("/profile?alert=Please+enter+your+health+profile+to+get+personalized+diet+plan")

    weight, height, activity, diseases, age, gender = profile

    # BMI Calculation
    bmi = calculate_bmi(weight, height)
    bmi_status = bmi_category(bmi)

    # Daily Calorie Requirement
    calories_needed = calculate_daily_calories(weight, activity)

    # Decide Diet Type - Enhanced with age and gender
    diet_type = decide_diet_type(bmi, diseases)
    
    # Further refine based on age
    if age and age < 25:
        if "Diabetic" not in diet_type:
            diet_type = "Normal" if diet_type == "Normal" else diet_type
    elif age and age > 50:
        if diet_type == "Weight Loss":
            diet_type = "Normal"

    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Fetch Meals for All Days - With fresh randomization each time
    # Using RANDOM() twice ensures different ordering on each page load
    cur.execute("""
        SELECT food, 1 as quantity, 'serving' as unit, calories, protein, carbs, fats, meal, day
        FROM module2_diet
        WHERE diet=?
        ORDER BY
            CASE day
                WHEN 'Monday' THEN 1
                WHEN 'Tuesday' THEN 2
                WHEN 'Wednesday' THEN 3
                WHEN 'Thursday' THEN 4
                WHEN 'Friday' THEN 5
                WHEN 'Saturday' THEN 6
                WHEN 'Sunday' THEN 7
            END,
            CASE meal
                WHEN 'Breakfast' THEN 1
                WHEN 'Lunch' THEN 2
                WHEN 'Snack' THEN 3
                WHEN 'Dinner' THEN 4
            END,
            RANDOM(),
            RANDOM()
    """, (diet_type,))
    all_meals = cur.fetchall()
    con.close()

    # Organize Meals by Day and Meal Type
    meals_by_day = {day: {"Breakfast": [], "Lunch": [], "Snack": [], "Dinner": []} for day in days_list}

    for m in all_meals:
        food, quantity, unit, calories, protein, carbs, fats, meal_type, meal_day = m
        meals_by_day[meal_day][meal_type].append({
            "food": food,
            "quantity": quantity,
            "unit": unit,
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fats": fats
        })

    # Total Calories Today
    today = datetime.datetime.now().strftime("%A")
    total_calories = sum(m["calories"] * m["quantity"] for meal_type in meals_by_day[today].values() for m in meal_type)

    # Junk Food Detection
    junk_items = ["Burger", "Pizza", "Fried Rice", "Noodles", "Ice Cream"]
    junk_found = [m["food"] for meal_type in meals_by_day[today].values() for m in meal_type if m["food"] in junk_items]
    junk_alert = "Junk food detected: " + ", ".join(junk_found) if junk_found else "No junk food detected. Good eating habit"

    # Water Intake Reminder
    water_liters = round(weight * 0.033, 1)
    water_reminder = f"Drink at least {water_liters} liters of water today."

    # Diet Suggestion
    suggestions = {
        "Weight Loss": "Avoid fried foods, eat more vegetables, and walk daily.",
        "Muscle Gain": "Increase protein intake and include strength training.",
        "Diabetic": "Avoid sugar, white rice, and sweetened drinks.",
        "Normal": "Maintain balanced meals and regular eating habits."
    }
    suggestion = suggestions.get(diet_type)

    # Nutrient Distribution
    nutrient_distribution = {
        "Carbohydrates": "50–55%",
        "Proteins": "20–25%",
        "Fats": "20–25%",
        "Fiber": "High"
    }

    response = make_response(render_template(
        "diet.html",
        bmi=bmi,
        bmi_status=bmi_status,
        calories_needed=calories_needed,
        diet_type=diet_type,
        meals_by_day=meals_by_day,
        nutrients=nutrient_distribution,
        total_calories=total_calories,
        junk_alert=junk_alert,
        water_reminder=water_reminder,
        suggestion=suggestion,
        days_list=days_list,
        selected_day=today,
        success_msg=request.args.get('success')
    ))
    
    # Add cache-busting headers to ensure fresh data on each load
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response

 

@app.route("/module3", methods=["GET", "POST"])
def module3():
    if "user_id" not in session:
        return redirect("/login")
    
    # Check if health profile exists
    con_check = get_db()
    cur_check = con_check.cursor()
    cur_check.execute("SELECT id FROM health_profile WHERE user_id=? LIMIT 1", (session["user_id"],))
    profile_exists = cur_check.fetchone()
    con_check.close()
    
    if not profile_exists:
        return redirect("/profile?alert=Please+enter+your+health+profile+to+access+this+service")
    
    result = None

    if request.method == "POST":
        symptom = request.form["symptom"]
        severity = request.form["severity"]
        days = int(request.form["days"])

        con = get_db()
        cur = con.cursor()

        cur.execute("""
        SELECT condition, medicine, consult
        FROM module3_symptoms
        WHERE symptom=? AND severity=? AND days<=?
        ORDER BY days DESC
        LIMIT 1
        """, (symptom, severity, days))

        result = cur.fetchone()
        con.close()

    return render_template("module3.html", result=result)

# ---------------- MEDICINES ----------------
@app.route("/medicines", methods=["GET", "POST"])
def medicines():
    if "user_id" not in session:
        return redirect("/login")
    
    # Check if health profile exists
    con_check = get_db()
    cur_check = con_check.cursor()
    cur_check.execute("SELECT id FROM health_profile WHERE user_id=? LIMIT 1", (session["user_id"],))
    profile_exists = cur_check.fetchone()
    con_check.close()
    
    if not profile_exists:
        return redirect("/profile?alert=Please+enter+your+health+profile+to+access+this+service")

    con = get_db()
    cur = con.cursor()

    # Handle form submission
    if request.method == "POST":
        cur.execute("""
            INSERT INTO module4_medicines
            (name, dosage, frequency, duration, warning)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form["name"],
            request.form["dosage"],
            request.form["frequency"],
            request.form["duration"],
            request.form["warning"]
        ))
        con.commit()

    # Fetch saved medicines
    cur.execute("SELECT * FROM module4_medicines")
    medicines = cur.fetchall()
    con.close()

    return render_template("medicines.html", medicines=medicines)


# ---------------- PHARMACY ----------------
@app.route("/pharmacy")
def pharmacy():
    if "user_id" not in session:
        return redirect("/login")
    
    # Check if health profile exists
    con_check = get_db()
    cur_check = con_check.cursor()
    cur_check.execute("SELECT id FROM health_profile WHERE user_id=? LIMIT 1", (session["user_id"],))
    profile_exists = cur_check.fetchone()
    con_check.close()
    
    if not profile_exists:
        return redirect("/profile?alert=Please+enter+your+health+profile+to+access+this+service")

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM pharmacy_availability_dataset")
    pharmacies = cur.fetchall()
    con.close()

    return render_template("pharmacy.html", pharmacies=pharmacies)
#module 5
@app.route("/consultation", methods=["GET", "POST"])
def consultation():
    if "user_id" not in session:
        return redirect("/login")
    
    # Check if health profile exists
    con_check = get_db()
    cur_check = con_check.cursor()
    cur_check.execute("SELECT id FROM health_profile WHERE user_id=? LIMIT 1", (session["user_id"],))
    profile_exists = cur_check.fetchone()
    con_check.close()
    
    if not profile_exists:
        return redirect("/profile?alert=Please+enter+your+health+profile+to+access+this+service")
  
    con = get_db()
    cur = con.cursor()
    if request.method == "POST" and "add_record" in request.form:
        weight = request.form.get("weight")
        symptom = request.form.get("symptom")
        severity = request.form.get("severity")
        days = int(request.form.get("days_persisted", 0))
        doctor_alert = "Yes" if severity == "Severe" or days > 3 else "No"
        emergency_flag = "RED" if severity == "Severe" and days > 1 else "Normal"
        cur.execute("INSERT INTO health_monitoring_dataset (user_id, weight, symptom, severity, days_persisted, doctor_alert, emergency_flag, remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (session["user_id"], weight, symptom, severity, days, doctor_alert, emergency_flag, "Keep tracking"))
        con.commit()
    search_query = request.args.get("search", "")
    if search_query:
        cur.execute("SELECT * FROM module5_doctors WHERE specialization LIKE ?", ('%' + search_query + '%',))
    else:
        cur.execute("SELECT * FROM module5_doctors LIMIT 10")
    doctors = cur.fetchall()
    cur.execute("SELECT * FROM health_monitoring_dataset WHERE user_id=? ORDER BY record_id DESC", (session["user_id"],))
    health_history = cur.fetchall()
    con.close()
    return render_template("consultation.html", doctors=doctors, health_history=health_history)

@app.route("/delete_record/<int:id>")
def delete_record(id):
    con = get_db()
    con.execute("DELETE FROM health_monitoring_dataset WHERE record_id=?", (id,))
    con.commit()
    con.close()
    return redirect("/consultation")


# ---------------- ADMIN LOGIN ----------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = get_db()
        cur = con.cursor()
        cur.execute(
            "SELECT id FROM admins WHERE username=? AND password=?",
            (username, password)
        )
        admin = cur.fetchone()
        con.close()

        if admin:
            session["admin_id"] = admin[0]
            return redirect("/admin_dashboard")
       

    return render_template("admin_login.html")

# ---------------- ADMIN DASHBOARD ----------------

@app.route("/admin_dashboard")
def admin_dashboard():
    if "admin_id" not in session:
        return redirect("/login")

    # Connect to database and set row_factory to return dict-like rows
    con = get_db()
    con.row_factory = sqlite3.Row  # <-- key fix
    cur = con.cursor()

    # Fetch all tables
    health = cur.execute("SELECT * FROM health_monitoring_dataset").fetchall()
    doctors = cur.execute("SELECT * FROM module5_doctors").fetchall()
    medicines = cur.execute("SELECT * FROM module4_medicines").fetchall()
    pharmacy = cur.execute("SELECT * FROM pharmacy_availability_dataset").fetchall()
    symptoms = cur.execute("SELECT * FROM module3_symptoms").fetchall()
    diet = cur.execute("SELECT * FROM module2_diet").fetchall()

    con.close()

    # Render template with dictionary-like rows
    return render_template(
        "admin_dashboard.html",
        health=health,
        doctors=doctors,
        medicines=medicines,
        pharmacy=pharmacy,
        symptoms=symptoms,
        diet=diet
    )

# ---------------- ADD ----------------
@app.route("/add/<table>", methods=["POST"])
def add(table):
    if "admin_id" not in session:
        return redirect("/login")
    con = get_db()
    cur = con.cursor()
    data = request.form.to_dict()
    
    if table == "health":
        cur.execute("""INSERT INTO health_monitoring_dataset 
            (user_id, weight, symptom, severity, days_persisted, doctor_alert, emergency_flag, remarks)
            VALUES (:user_id,:weight,:symptom,:severity,:days_persisted,:doctor_alert,:emergency_flag,:remarks)""", data)
    elif table == "doctors":
        cur.execute("""INSERT INTO module5_doctors (doctor,specialization,hospital,availability)
                       VALUES (:doctor,:specialization,:hospital,:availability)""", data)
    elif table == "medicines":
        cur.execute("""INSERT INTO module4_medicines (name,dosage,frequency,duration,warning)
                       VALUES (:name,:dosage,:frequency,:duration,:warning)""", data)
    elif table == "pharmacy":
        cur.execute("""INSERT INTO pharmacy_availability_dataset (pharmacy_name,location,medicine_name,stock,contact)
                       VALUES (:pharmacy_name,:location,:medicine_name,:stock,:contact)""", data)
    elif table == "symptoms":
        cur.execute("""INSERT INTO module3_symptoms (symptom,severity,days,condition,medicine,consult)
                       VALUES (:symptom,:severity,:days,:condition,:medicine,:consult)""", data)
    elif table == "diet":
        cur.execute("""INSERT INTO module2_diet (food,calories,protein,carbs,fats,diet,meal)
                       VALUES (:food,:calories,:protein,:carbs,:fats,:diet,:meal)""", data)
    con.commit()
    con.close()
    return redirect("/admin_dashboard")
@app.route("/delete/<table>/<int:id>")
def delete(table, id):
    if "admin_id" not in session:
        return redirect("/login")
    
    con = get_db()
    cur = con.cursor()
    
    mapping = {
        "health":"health_monitoring_dataset",
        "doctors":"module5_doctors",
        "medicines":"module4_medicines",
        "pharmacy":"pharmacy_availability_dataset",
        "symptoms":"module3_symptoms",
        "diet":"module2_diet"
    }

    # define which columns exist for each table
    columns_mapping = {
        "health": ["id", "record_id"],
        "doctors": ["id"],
        "medicines": ["id"],
        "pharmacy": ["id", "pharmacy_id"],
        "symptoms": ["id"],
        "diet": ["id"]
    }

    columns = columns_mapping[table]
    placeholders = " OR ".join([f"{col}=?" for col in columns])
    values = tuple([id]*len(columns))
    
    cur.execute(f"DELETE FROM {mapping[table]} WHERE {placeholders}", values)
    con.commit()
    con.close()
    
    return redirect("/admin_dashboard")




# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
 
