import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
# # Create table w/o PK.
# # dbCursor.execute("CREATE TABLE customers (name varchar(255), address varchar(255))")

# Create table with PK.
dbCursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), address varchar(255))")

# # Add PK to an existing table.
# dbCursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Check if table exists.
dbCursor.execute("SHOW TABLES")
for x in dbCursor:
    print(x)

cnx.close()
