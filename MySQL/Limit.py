import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
dbCursor.execute("SELECT * FROM customers LIMIT 5")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

cnx.close()
