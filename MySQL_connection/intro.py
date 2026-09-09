import mysql.connector

#Creates or gets a MySQL connection object.
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10"
)

print(mydb)
