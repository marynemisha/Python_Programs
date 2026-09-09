import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
cursor=mydb.cursor()

#id,name,place,company,age,salary
id=int(input("Enter your id:"))
name=input("Enter your name:")
place=input("Enter your location:")
company=input("Enter your company:")
age=int(input("Enter your age:"))
salary=int(input("Enter your salary:"))

query="""
    INSERT INTO employee(id,name,place,company,age,salary)
    VALUES(%s,%s,%s,%s,%s,%s)
"""
values=(id,name,place,company,age,salary)
cursor.execute(query,values)
mydb.commit()
print("New employee record inserted...!")

cursor.execute("SELECT * FROM employee")
result=cursor.fetchall()
for emp in result:
    print(emp)

