import mysql.connector
import datetime
class BloodDonorManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nemisha@10",
            database="blood_db"
        )
        print("Database connected successfully...!")
    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = ("insert into donor(name,blood_group,phone,city,last_donation)values(%s,%s,%s,%s,%s)")
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor added successfully....!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            # print(records)
            # for data in records:
            #     print(data)
            return records
        except Exception as e:
            return []

    def retrieve(self,id=None):
        try:
            record = self.get_object(id=id)
            if record==None:
                print("Donor not found..!")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record = self.get_object(id=id)
            values=(id,)
            if record!=None:
                query="delete from donor where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor deleted successfully...!")
            else:
                print("Donor not found...!")
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor = self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s",
                    placeholder=placeholder.rstrip(",")
                    query=f"update donor set {placeholder} where id=%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor details updated successfully....!")
        except Exception as e:
            print(e)

donor_instance=BloodDonorManager()
# donor_instance.post(name="Anju",blood_group="AB+",phone="9876543210",city="Ernakulam",last_donation=datetime.datetime.today())
# donor_instance.post(name="Anjali",blood_group="A+",phone="9876543212",city="Ernakulam",last_donation=datetime.datetime.today())
# donor_instance.post(name="Anu",blood_group="B+",phone="9876543260",city="TVM",last_donation=datetime.datetime.today())
donor_instance.post(name="Rahul",blood_group="o+",phone="9876543299",city="Kakkanad",last_donation=datetime.datetime.today())
# donor_instance.post(name="Ram",blood_group="o+",phone="9876540299",city="Kakkanad",last_donation=datetime.datetime.today())
# donor_instance.get()
# donor_instance.retrieve(id=1)
# donor_instance.retrieve(id=10)
# donor_instance.retrieve(id=4)
# donor_instance.delete(id=10)
# donor_instance.delete(id=4)
# print("...........After deleting a donor..........")
# donor_instance.get()