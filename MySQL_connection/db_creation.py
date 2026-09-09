import mysql.connector

#Creates or gets a MySQL connection object.
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10"
)
#used to execute sql commands for python
mycursor=mydb.cursor()
mycursor.execute("create database Companydb")
print("Database created successfully...!")
mycursor.execute("SHOW DATABASES")
print(mycursor.fetchall())
