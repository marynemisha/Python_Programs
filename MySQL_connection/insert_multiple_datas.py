import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)

obj=mydb.cursor()
#id,name,place,company,age,salary
employees=[
    (6,"Ashna","Kaloor","Luminar",23,20000),
    (7,"Vinay","Thrissur","Wipro",32,90000)
]

query="""
       INSERT INTO employee(id,name,place,company,age,salary)
       VALUES(%s,%s,%s,%s,%s,%s)
"""

obj.executemany(query,employees)
mydb.commit()