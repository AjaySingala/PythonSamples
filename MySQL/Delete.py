import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
dbCursor.execute("DELETE FROM Customers WHERE address = 'Mountain 21'")

cnx.commit()
print(dbCursor.rowcount, "record(s) deleted")

# DELETE by preventing SQL Injection.
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
dbCursor.execute(sql, adr)

cnx.commit()
print(dbCursor.rowcount, "record(s) deleted")

cnx.close()
