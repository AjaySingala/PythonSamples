import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

dbCursor.execute(sql)
cnx.commit()        # on the connection, not cursor.

# print row count.
print(dbCursor.rowcount, "row(s) affected.")

cnx.close()
