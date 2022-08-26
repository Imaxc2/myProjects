import pymysql
from mysqlka import host, user, password, db_name
host = 'localhost'
user = 'root'
password = ''
db_name = 'Telegram'

def add_id(teg):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                find_id = "SELECT * FROM `users` WHERE fullid = %s"
                cursor.execute(find_id, teg)
                rows = cursor.fetchall()
                if len(rows) < 1:
                    insert_query = "INSERT INTO `users` (money, fullid) VALUES (1000, %s)"
                    cursor.execute(insert_query, teg)
                    connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def get_money(teg):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                find_id = "SELECT * FROM `users` WHERE fullid = %s"
                cursor.execute(find_id, teg)
                rows = cursor.fetchall()
                money = rows[0].get('money')
                return money
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)