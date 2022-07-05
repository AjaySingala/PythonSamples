import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Reston, VA")

dbCursor.execute(sql, val)
cnx.commit()        # on the connection, not cursor.

# print row count.
print(dbCursor.rowcount, "records inserted.")

cnx.close()
