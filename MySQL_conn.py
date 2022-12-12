# pip install mysql-connector-python

import mysql.connector

config = {
    'user': 'root',
    'password': 'helloworld',
    'host': '127.0.0.1',   # Or an IP Address that your DB is hosted on
    'port': '3306',
    'database': 'eduridge',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)
cursor.execute("show tables;")

data = cursor.fetchall()
print(data)

