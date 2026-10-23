import mysql.connector
class Dbconnect:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nemisha@10",
                database="healthdb"
            )
            return self.connection
        except Exception as e:
            return None
class PatientManager(Dbconnect):
    pass