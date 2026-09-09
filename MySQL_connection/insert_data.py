import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
obj=mydb.cursor()
query="""
      INSERT INTO employee(id,name,place,company,age,salary)
      VALUES(1,"Rahul","Aluva","Luminar",35,80000),
      (2,"Teena","Kakkanad","TCS",30,75000),
      (3,"Gautham","Edapally","TCS",27,65000),
      (4,"Shyam","Edapally","Infosys",29,60000),
      (5,"Anu","Ernakulam","Wipro",25,30000)
"""

obj.execute(query)
mydb.commit()
print("Employee data inserted successfully")