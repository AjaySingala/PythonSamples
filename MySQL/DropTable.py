import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
sql = "DROP TABLE customers"
dbCursor.execute(sql)

# Check if table exists.
dbCursor.execute("SHOW TABLES")
for x in dbCursor:
    print(x)

cnx.close()
