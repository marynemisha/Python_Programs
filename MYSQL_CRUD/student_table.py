import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
cursor=mydb.cursor()
query="""
      create table student1(
      id int primary key,
      name varchar(100),
      age int,
      place varchar(100),
      course varchar(100),
      mobile bigint,
      college varchar(100))
"""
cursor=cursor.execute(query)
print("Student table created successfully...!")
