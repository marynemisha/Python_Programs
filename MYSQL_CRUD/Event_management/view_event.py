import mysql.connector

class EventManager:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nemisha@10",
            database="event_db"
        )
        print("Connected successfully...!")
    def get_object(self, id=None):
        try:
            self.cursor = self.con.cursor()
            query = "select * from event where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def post(self,**kwargs):
        try:
            self.cursor = self.con.cursor()
            query = ("insert into event(event_name,event_type,venue,organizer,phone,event_date)values(%s,%s,%s,%s,%s,%s)")
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.con.commit()
            print("Event added successfully....!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.con.cursor()
            query = "select * from event"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("Event not found..!")
            print(record)
        except Exception as e:
            print(e)
    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from event where id=%s"
                self.cursor.execute(query, values)
                self.con.commit()
                print("Event deleted successfully...!")
            else:
                print("Event not found...!")
        except Exception as e:
            print(e)
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.con.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder = placeholder.rstrip(",")
                query = f"update event set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.con.commit()
                print("Event details updated successfully....!")
        except Exception as e:
            print(e)

event=EventManager()
# event.post(event_name="Onam Celebration",event_type="Festival",venue="Kochi",organizer="Luminar",phone="9876543210",event_date="2026-09-05")
# event.post(event_name="Tech Fest",event_type="Technology",venue="TVM",organizer="Technopark",phone="9876543211",event_date="2026-09-10")
# event.post(event_name="Music Night",event_type="Music",venue="Kochi",organizer="Musical Events",phone="9876543212",event_date="2026-09-15")
# event.post(event_name="Sports Meet",event_type="Sports",venue="Kottayam",organizer="Sports Association",phone="9876543214",event_date="2026-09-25")
# event.get()
# event.retrieve(id=1)
# event.delete(id=3)
event.put(id=5,event_name="Sports Meet 2026",event_type="Sports",venue="Kochi",organizer="Sports Association",phone="9876543214",event_date="2026-09-28")
event.get()