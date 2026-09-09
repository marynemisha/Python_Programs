import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
obj=mydb.cursor()
query="SELECT * FROM employee"
obj.execute(query)
result=obj.fetchall()
#print(result)
for emp in result:
    print(emp)

print("Get the details of one employee______")
obj.execute("SELECT * FROM employee")
employee=obj.fetchone()
print(employee)
