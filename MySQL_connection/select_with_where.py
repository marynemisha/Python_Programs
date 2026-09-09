import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)

obj=mydb.cursor()
query="select * from employee where id=3"
obj.execute(query)
result=obj.fetchone()
print(result)

query="select * from employee where company='Luminar'"
obj.execute(query)
result=obj.fetchall()
#print(result)
print("Employees from Luminar:")
for emp in result:
    print(emp)

query="select * from employee where place='Ernakulam'"
obj.execute(query)
result=obj.fetchall()
print("Employees from Ernakulam:")
for emp in result:
    print(emp)