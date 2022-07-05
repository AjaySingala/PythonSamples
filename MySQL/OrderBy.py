import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
dbCursor.execute("SELECT * FROM Customers ORDER BY name")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

# ORDER BT DESC.
print("\nORDER BY DESC...")
dbCursor.execute("SELECT * FROM Customers ORDER BY name DESC")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

cnx.close()
