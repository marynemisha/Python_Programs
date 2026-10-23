import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nemisha@10",
    database="companydb"
)
cursor=mydb.cursor()
#insert values
query="""
      INSERT INTO student1(id,name,age,place,course,mobile,college)
      VALUES(%s,%s,%s,%s,%s,%s,%s)
"""
values=[(1,"Rahul",35,"Aluva","BCA",9876543210,"KMM"),
      (2,"Teena",28,"Kakkanad","MTECH",8675210443,"LF")]
# cursor.execute(query,values)
mydb.commit()
print("Student data inserted successfully...!")

#select (view details)
cursor.execute("SELECT * from student1")
result=cursor.fetchall()
print(".....STUDENT DETAILS.....")
for stud in result:
    print(stud)


#update
query="""
    UPDATE student1 set place="Trivandrum" where id=1
"""
cursor.execute(query)
mydb.commit()
print("Student data updated....!")

#select (view updated data details)
cursor.execute("SELECT * from student1")
result=cursor.fetchone()
print(".....STUDENT DETAILS.....")
print(result)

# delete data
query="""delete from student1 where id=2
"""
cursor.execute(query)
mydb.commit()
print("Student data deleted....!")

#select (view deleted data details)
cursor.execute("SELECT * from student1")
result=cursor.fetchone()
print(".....STUDENT DETAILS.....")
print(result)


#close connection
cursor.close()
mydb.close()

