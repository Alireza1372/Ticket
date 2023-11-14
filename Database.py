import mysql.connector


class MyDatabase:
    def __init__(self):
        db_config = {
            "host": "localhost",
            "user": "root",

        }
        self.hand = self.hand = mysql.connector.connect(**db_config)
        self.cur = self.cur = self.hand.cursor()

    def create_db(self,db_name):
        create_database_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        self.cur.execute(create_database_query)
        self.hand.database = "ticket"

    def create_table(self, name):
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            date VARCHAR(255) NOT NULL
        )
        """
        self.cur.execute(create_table_query)
        self.hand.commit()

    def insert_data(self, username, city, date):
        insert_data_table_query = "INSERT INTO user (username, city, date) VALUES (%s, %s,%s)"
        data = [(username, city, date)]

        self.cur.executemany(insert_data_table_query, data)

        self.hand.commit()

    def get_data(self):
        select_data_query = "SELECT * FROM user"
        self.cur.execute(select_data_query)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def delete_all_table_data(self):
        delete_all_data_query = "DELETE FROM user"
        self.cur.execute(delete_all_data_query)
        self.hand.commit()

    def delete_db(self):
        drop_database_query = "DROP DATABASE IF EXISTS ticket"
        self.cur.execute(drop_database_query)
        self.hand.commit()

    def close_db(self):
        self.cur.close()
        self.hand.close()

    def search_by_name(self, username):
        search_query = "SELECT * FROM user WHERE username = %s"
        search_value = (username,)  #
        self.cur.execute(search_query, search_value)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def search_by_city(self, city):
        search_query = "SELECT * FROM user WHERE city = %s"
        search_value = (city,)  #
        self.cur.execute(search_query, search_value)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        return rows


#newdb = MyDatabase()
#newdb.delete_db()
#newdb.create_db()
#newdb.create_table("user")
#newdb.delete_all_table_data()
#newdb.insert_data("alireza", "paris", "1372/04/22")
#newdb.insert_data("alireza", "paris", "1395/04/22")
#newdb.insert_data("reza", "Tehran", "1382/04/22")
#newdb.insert_data("ali", "paris", "1392/04/22")
#newdb.get_data()
print("****")
#newdb.search_by_name("alireza")
print("****")
#newdb.search_by_city("paris")
#newdb.close_db()
