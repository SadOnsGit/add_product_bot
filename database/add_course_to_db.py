from getpass import getpass
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()

mysql_login = os.getenv('mysql_login')
mysql_password = os.getenv('mysql_password')
host = os.getenv('host')
db_name = os.getenv('db_name')


async def add_course_to_db(name: str, desc: str, price: int, prod_url: str):
    try:
        with connect(
            host=f"{host}",
            user=f"{mysql_login}",
            password=f"{mysql_password}",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO u2556815_products.item (title, price, text, prod_url) VALUES (%s, %s, %s, %s)', (name, price, desc, prod_url))
            connection.commit()
    except Error as e:
        print(e)