import mysql.connector

cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Password@123',
    database='ecommerce'
)

dbCursor = cnx.cursor()
dbCursor.execute("SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id")

rows = dbCursor.fetchall()
for row in rows:
    print(row)

cnx.close()
