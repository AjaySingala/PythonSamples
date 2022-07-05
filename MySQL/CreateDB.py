import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123'
)

dbCursor = cnx.cursor()
dbCursor.execute("CREATE DATABASE ecommerce")

cnx.close()
