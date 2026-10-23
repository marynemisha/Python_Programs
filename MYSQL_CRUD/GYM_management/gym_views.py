import mysql.connector
import datetime
class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nemisha@10",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None
class GymMemberManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            # print(records)
            return records
        except Exception as e:
            return []
    def post(self,**kwargs):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query="insert into member(name,place,mobile,plan,fee,joined_on)values(%s,%s,%s,%s,%s,%s)"
        values=[v for v in kwargs.values()]
        self.cursor.execute(query, values)
        self.connection.commit()
        print("New member added successfully..!")
    def retrieve(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            records = self.get_object(id=id)
            if records==None:
                print("Member not found...!")
            else:
                print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            records = self.get_object(id=id)
            if records==None:
                print("Member not found...!")
            else:
                query="delete from member where id=%s"
                values=(id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member deleted successfully...!")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            self.connect=super().get_connection()
            self.cursor = self.connect.cursor()
            records= self.get_object(id=id)
            if records==None:
                print("Member not found...!")
            else:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update member set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member updated successfully...!")
        except Exception as e:
            print(e)

connection_instance=DbConnect()
print(connection_instance.get_connection())

member_instance=GymMemberManager()
#member_instance.get()
#member_instance.post(name="Ammu",place="Ekm",mobile="9876543211",plan="1 year",fee=10000,joined_on=datetime.datetime.today())
#member_instance.post(name="Dev",place="Ktym",mobile="9876500211",plan="6 months",fee=5000,joined_on=datetime.datetime.today())
#member_instance.post(name="Devan",place="Ktym",mobile="7876500211",plan="2 months",fee=2000,joined_on=datetime.datetime.today())
# member_instance.get()
# member_instance.retrieve(id=1)
# member_instance.delete(id=3)
# member_instance.put(id=1,name="Anu",place="Ktym",mobile="9876500211",plan="6 months",fee=5000,joined_on=datetime.datetime.today())
# member_instance.get()
# member_instance.retrieve(id=1)
# member_instance.delete(id=2)