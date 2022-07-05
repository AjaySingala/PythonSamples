import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
dbCursor.execute("SELECT * FROM Customers")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

# Selecting Columns.
print("\nSelecting Columns...")
dbCursor.execute("SELECT name, address FROM Customers")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

# Fetch first record.
print("\nFetching first record using fetchone()...")
dbCursor.execute("SELECT * FROM customers")

row = dbCursor.fetchone()

print(row)

cnx.close()
