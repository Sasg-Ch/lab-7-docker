from main import db_connect
import mysql.connector
import faker
import random

connection = db_connect()
cursor = connection.cursor()
cursor.execute("USE mydb")

fake = faker.Faker()

item_names = ['Футболка', 'Штани', 'Сукня', 'Спідниця', 'Светр', 'Куртка', 'Шорти', 'Чоботи', 'Кросівки', 'Сандалі', 'Шапка', 'Рукавички', 'Пальто', 'Топ', 'Сорочка', 'Костюм', 'Жилет']


for _ in range(3):
    storage_address = fake.address().replace("\n",", ")
    storage_manager = fake.name()
    phone = f"+380{random.randint(30,99)}-{random.randint(100,999)}-{random.randint(1000,9999)})"
    cursor.execute("""
            INSERT INTO Storages (storage_address, storage_manager, phone) 
            VALUES (%s, %s, %s)
        """, (storage_address, storage_manager, phone))

for _ in range(7):
    customer_name = fake.name()
    customer_address = fake.address().replace("\n",", ")
    phone = f"+380{random.randint(30,99)}-{random.randint(100,999)}-{random.randint(1000,9999)})"
    contact_person = fake.name()
    cursor.execute("""
            INSERT INTO Customers (customer_name, customer_address, phone, contact_person) 
            VALUES (%s, %s, %s, %s)
        """, (customer_name, customer_address, phone,contact_person))

for _ in range(17):
    type = random.choice(['Жіночий','Чоловічий','Дитячий'])
    name_item = random.choice(item_names) + ' ' + fake.word().capitalize()
    maker = fake.company()
    storage_id = random.randint(1,3)
    quantity = random.randint(1,30)
    price = round(random.uniform(5,100),2)
    cursor.execute("""
            INSERT INTO Items (type, name_item, maker,storages_id,quantity,price) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (type, name_item, maker,storage_id,quantity,price))

for _ in range(22):
    customer_code = random.randint(1,7)
    code_item = random.randint(1,17)
    sold_count = random.randint(1,10)
    discount = round(random.uniform(0, 50), 2)
    cursor.execute("""
            INSERT INTO Sales (customer_code, code_item, sold_count,discount) 
            VALUES (%s, %s, %s, %s)
        """, (customer_code, code_item, sold_count,discount))

connection.commit()

cursor.close()
connection.close()