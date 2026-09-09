import mysql.connector

#Creates or gets a MySQL connection object.
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10"
)

obj=mydb.cursor()
obj.execute("SELECT VERSION()")
print(obj.fetchone())

obj.execute("SHOW DATABASES")
print(obj.fetchall())