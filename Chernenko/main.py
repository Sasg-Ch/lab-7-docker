import mysql.connector

def db_connect():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="myuser",
        password="mypassword"
    )
    return connection

connection = db_connect()
cursor = connection.cursor()

cursor.execute("USE mydb")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Storages (
        storages_id INT AUTO_INCREMENT PRIMARY KEY,
        storage_address VARCHAR(255) NOT NULL,
        storage_manager VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Items (
        code_item INT AUTO_INCREMENT PRIMARY KEY,
        type ENUM('Жіночий','Чоловічий','Дитячий') NOT NULL,
        name_item VARCHAR(255) NOT NULL,
        maker VARCHAR(255) NOT NULL,
        storages_id INT NOT NULL,
        quantity INT NOT NULL,
        price decimal(10,2) NOT NULL,
        FOREIGN KEY (storages_id) REFERENCES Storages(storages_id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_code INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(255) NOT NULL,
        customer_address VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        contact_person VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        sale_code INT AUTO_INCREMENT PRIMARY KEY,
        sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        customer_code INT NOT NULL,
        code_item INT NOT NULL,
        sold_count INT NOT NULL,
        discount DECIMAL(10, 2) DEFAULT 0,
        FOREIGN KEY (customer_code) REFERENCES Customers(customer_code),
        FOREIGN KEY (code_item) REFERENCES Items(code_item)
    )
""")

print("OK")

# Закриття з'єднання
cursor.close()
connection.close()
