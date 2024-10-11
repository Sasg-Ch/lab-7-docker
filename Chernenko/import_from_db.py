from main import db_connect
import mysql.connector
from prettytable import from_db_cursor


def output_from_db(name_table):
    cursor.execute(f"SELECT * FROM {name_table}")
    mytable = from_db_cursor(cursor)
    print(mytable)

connection = db_connect()
cursor = connection.cursor()
cursor.execute("USE mydb")

tables = ['storages','Customers','Items','Sales']
for table in tables:
    print(f"Таблиця {table}")
    output_from_db(table)
    print('\n')

cursor.close()
connection.close()