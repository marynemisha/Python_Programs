import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
obj=mydb.cursor()

query="""
      UPDATE employee set place="Trivandrum"
      where id=1
"""

obj.execute(query)
mydb.commit()
print("Data updated successfully")

print("---After Updation---")
query="select * from employee where id=1"
obj.execute(query)
result=obj.fetchone()
print(result)

print("--Delete data--")
query="delete from employee where id=5"
obj.execute(query)
mydb.commit()

query="select * from employee"
obj.execute(query)
result=obj.fetchall()
for row in result:
    print(row)