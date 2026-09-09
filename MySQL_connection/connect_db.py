import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
print("Connected to MySQL Database")
obj=mydb.cursor()
query="""
      CREATE TABLE Employee(
      id int primary key,
      name varchar(200),
      place varchar(200),
      company varchar(200),
      age int,
      salary int)
"""
obj.execute(query)
print("Table created successfully...!")